"""Graphiti + Neo4j Community backend for :class:`IAudienceStore`.

Shipping default for *local production* runs of the simulator. Wraps
the upstream ``graphiti-core`` library (Apache 2.0, same vendor as Zep
Cloud) against a local Neo4j Community instance (GPLv3, composes with
this repository's AGPLv3) launched via ``backend/docker-compose.yml``.

Two impedance mismatches motivate the structure here:

1. **Graphiti is async-first; :class:`IAudienceStore` is sync.** Each
   Protocol method funnels its Graphiti call through :meth:`_run`, which
   drives a private :mod:`asyncio` event loop. We deliberately do NOT
   widen the Protocol to async -- that would force every consumer
   (``simulation_runner`` and friends) into async/await and force the
   mock backend to grow a coroutine surface it does not need.

2. **The 2 read-surface methods (``filter_defined_entities`` /
   ``get_entities_by_type``) do not map 1:1 onto Graphiti's public
   API.** Graphiti exposes node/edge CRUD via its async driver but does
   not expose a "give me all nodes of type T" entry point. We reach
   through ``graphiti.driver`` and issue parameterised Cypher --
   portable to any Cypher-speaking backend (Aura, self-hosted
   Enterprise) if the user later migrates off Community.

graphiti-core's own types are typed loosely upstream; per the gate
constraint (no ``# pyright: ignore``) we type the *internal* Graphiti
return values as :data:`Any` at the call site and reconstruct our
strict :class:`EntityNode` / :class:`EntityEdge` / :class:`SearchResults`
shapes before returning. The Protocol-facing return types are never
widened.
"""
from __future__ import annotations

import asyncio
import importlib
import os
import threading
from typing import Any, Coroutine, Dict, List, Optional, TypeVar
from urllib.parse import urlparse


# ---------------------------------------------------------------------------
# Sync-bridge safety primitives (concurrency cap + per-call timeout)
# ---------------------------------------------------------------------------
#
# The Flask request thread enters :meth:`GraphitiAudienceStore._run`
# whenever a /api/sim/* handler reads from / writes to the audience
# store. Without a per-process cap, N concurrent Flask workers each
# spin a private event loop + a Neo4j round-trip + an LLM round-trip
# at the same time; Neo4j Community on a single host saturates fast
# under that pattern. The semaphore caps concurrent in-flight bridge
# calls so the seam degrades gracefully under load instead of
# hammering Neo4j.
#
# Default cap is 4, overridable via ``GRAPHITI_MAX_CONCURRENT_CALLS``
# so an operator with a beefier Neo4j tier can lift it. A cap of 1 is
# valid (full serialisation); a cap of 0 is rejected (would deadlock).
def _resolve_pos_int_env(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw is None:
        return default
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return default
    return value if value >= 1 else default


_GRAPHITI_MAX_CONCURRENT_CALLS: int = _resolve_pos_int_env(
    "GRAPHITI_MAX_CONCURRENT_CALLS", 4,
)
_GRAPHITI_CALL_TIMEOUT_S: int = _resolve_pos_int_env(
    "GRAPHITI_CALL_TIMEOUT_SEC", 60,
)
# threading.BoundedSemaphore (not Semaphore) so an accidental extra
# release raises ValueError at test time -- catches a refactor that
# double-counts a release.
_GRAPHITI_CALL_SEMAPHORE: "threading.BoundedSemaphore" = (
    threading.BoundedSemaphore(_GRAPHITI_MAX_CONCURRENT_CALLS)
)

from ..services.zep_entity_reader import EntityEdge, EntityNode, FilteredEntities
from .protocols import Episode, Ontology, SearchResults


T = TypeVar("T")


def llm_endpoint_is_openai_cloud(llm_base_url: str) -> bool:
    """Return True if ``llm_base_url`` is empty or resolves to OpenAI's cloud.

    Hostname-based rather than substring/prefix so the check survives every
    variation a user might paste in. Returns True (the "refuse" signal) for:

    * empty string / ``None`` — defaults to OpenAI cloud at the openai library
      level, so refuse it the same way an explicit cloud URL is refused.
    * any scheme + ``api.openai.com`` hostname + any port/path/trailing slash:
      ``https://api.openai.com``, ``https://api.openai.com/v1``,
      ``https://api.openai.com/v1/``, ``http://api.openai.com:80/v1``.
    * schemeless ``api.openai.com/v1`` (urlparse parks this in ``.path`` with
      ``.hostname=None``; the literal-prefix fallback catches it).

    Returns False for any other endpoint, e.g. ``http://localhost:11434/v1``,
    ``https://my-corp-proxy/openai/v1`` — the local-first contract treats
    those as the user's explicit opt-in.

    Single source of truth for the local-first refusal predicate; consumed by
    :class:`GraphitiAudienceStore.__init__`, ``MockZepStorage.get_factory``
    (the ``graphiti`` branch), and the integration-test skip helpers.
    """
    if not llm_base_url:
        return True
    parsed = urlparse(llm_base_url)
    host = (parsed.hostname or "").lower().strip()
    if host == "api.openai.com":
        return True
    # Schemeless URL such as "api.openai.com/v1": urlparse puts the whole
    # string in .path and leaves hostname=None. Catch the literal so the
    # refusal cannot be sidestepped by dropping the scheme.
    if llm_base_url.lower().strip().startswith("api.openai.com"):
        return True
    return False


def _import_graphiti_symbol(module: str, name: str) -> Any:
    """Dynamic import for optional ``graphiti-core`` symbols.

    Using :func:`importlib.import_module` rather than ``from graphiti_core
    import X`` keeps the symbol unresolved at type-check time so pyright
    does not emit ``reportMissingImports`` on mock/cloud envs where
    ``graphiti-core`` is intentionally absent. The returned value is
    typed :data:`Any`, which is what we want: every Graphiti object the
    store touches is reconstructed into one of our own Pydantic / dataclass
    shapes before crossing the seam boundary.
    """
    mod = importlib.import_module(module)
    return getattr(mod, name)


def _sanitize_uri(uri: str) -> str:
    """Return ``uri`` with any userinfo + query string stripped so error
    messages never leak credentials. Schemes + hosts + ports + paths
    are preserved so an operator can still see what was misconfigured.

    Two credential vectors handled:
      * ``user:password@host`` (userinfo in the authority component) --
        scrubbed by hostname extraction.
      * ``?api_key=...`` / ``?token=...`` (secret in the query string;
        common on corp-proxy URLs) -- scrubbed by always dropping
        ``parsed.query``. Fragment dropped too for the same reason.

    Pass-through cases (no credentials possible / nothing to strip):
      * empty string  -> unchanged
      * unparseable   -> unchanged
      * schemeless / no-authority forms with no `?` -> unchanged
    """
    if not uri:
        return uri
    try:
        parsed = urlparse(uri)
    except ValueError:
        return uri
    # No authority AND no query -> nothing to strip. A schemeless
    # ``host/path`` cannot carry userinfo, and absent ``?`` it cannot
    # carry a query-string secret either.
    if not parsed.netloc and not parsed.query and not parsed.fragment:
        return uri
    # Build the sanitised authority (drop userinfo when present).
    if parsed.netloc:
        host = parsed.hostname or ""
        if not host and "@" not in parsed.netloc:
            # Pathological: netloc exists but has no parseable host
            # and no userinfo to scrub; pass through verbatim.
            host_part = parsed.netloc
        else:
            port_suffix = f":{parsed.port}" if parsed.port else ""
            host_part = f"{host}{port_suffix}" if host else parsed.netloc.split("@")[-1]
        authority = f"{parsed.scheme}://{host_part}" if parsed.scheme else host_part
    else:
        # Schemeless input that still has a query/fragment -- preserve
        # whatever path was provided as-is sans the secret-carrying tail.
        authority = parsed.path or ""
        # In this branch parsed.path already holds the schemeless body;
        # we'll re-append below with query/fragment stripped.
        return authority
    return f"{authority}{parsed.path}"


def _entity_types_to_pydantic_classes(entity_types_dict: Any) -> Dict[str, Any]:
    """Convert ``{type_name: dict-schema-fragment}`` to ``{type_name:
    type[BaseModel]}`` using ``pydantic.create_model``.

    Upstream Graphiti's LLM extractor consumes ``entity_types`` as a
    mapping of type name to a Pydantic class so it can synthesise
    JSON-schema-driven extraction prompts and validate the extracted
    objects. The local protocol holds the dict form (wire-friendly,
    serialisable for tests); this helper bridges the two at the
    boundary so the on-disk ontology stays JSON-shaped while the
    extractor sees the typed shape.

    Dict-fragment shape (per ``app.seam.protocols.Ontology``):
      {
        "Stakeholder": {
            "description": "An audience segment ...",
            "properties": {
                "type": {"type": "string", "description": "..."},
                ...
            },
        },
        ...
      }

    Each fragment's ``properties`` are mapped to ``(str, Field(default=None, description=...))``
    tuples so the generated Pydantic class has the right field shape;
    type inference is conservative -- everything maps to ``str``
    unless the property dict carries an explicit ``type`` literal we
    recognise (``string``, ``integer``, ``number``, ``boolean``).
    """
    from pydantic import BaseModel, Field, create_model

    type_map: Dict[str, type] = {
        "string": str,
        "integer": int,
        "number": float,
        "boolean": bool,
    }
    out: Dict[str, Any] = {}
    for type_name, fragment in entity_types_dict.items():
        if not isinstance(fragment, dict):
            continue
        properties = fragment.get("properties") or {}
        description = fragment.get("description") or f"{type_name} entity."
        field_defs: Dict[str, Any] = {}
        for prop_name, prop_spec in properties.items():
            py_type: type = str
            prop_desc = ""
            if isinstance(prop_spec, dict):
                declared_type = prop_spec.get("type", "string")
                py_type = type_map.get(declared_type, str)
                prop_desc = prop_spec.get("description", "")
            field_defs[prop_name] = (
                Optional[py_type],
                Field(default=None, description=prop_desc),
            )
        model_cls = create_model(  # type: ignore[call-overload]
            type_name,
            __base__=BaseModel,
            __doc__=description,
            **field_defs,
        )
        out[type_name] = model_cls
    return out


class GraphitiInitError(RuntimeError):
    """Raised when the Graphiti client cannot connect / initialise.

    Distinct from ``RuntimeError`` so the factory and integration tests
    can discriminate "Neo4j unreachable" from "ZEP_MODE misconfigured".
    The exception message names ``NEO4J_URI`` so a misconfigured boot
    surfaces the env-var that needs fixing.
    """


# Map our Protocol's ``Episode.source`` string discriminator to
# Graphiti's ``EpisodeType`` enum. Keys mirror the docstring on
# :class:`app.seam.protocols.Episode`.
_EPISODE_SOURCE_MAP: Dict[str, str] = {
    "text": "text",
    "json": "json",
    "message": "message",
}


def _episode_type_for(source: str) -> Any:
    """Translate ``Episode.source`` -> ``graphiti_core.nodes.EpisodeType``.

    Imports the enum lazily so the module remains importable on machines
    that do not have ``graphiti-core`` installed (mock/cloud envs).
    Raises :class:`ValueError` -- never silently coerces -- on unknown
    sources so a typo (``"txt"`` instead of ``"text"``) fails loudly.
    """
    if source not in _EPISODE_SOURCE_MAP:
        raise ValueError(
            f"Episode.source={source!r} is not supported by "
            "GraphitiAudienceStore. Expected one of "
            f"{sorted(_EPISODE_SOURCE_MAP)!r}."
        )
    # EpisodeType is an enum whose member names line up with our source
    # strings. Use getattr so the lookup tolerates upstream enum
    # reordering without breaking the mapping.
    episode_type_cls = _import_graphiti_symbol("graphiti_core.nodes", "EpisodeType")
    return getattr(episode_type_cls, _EPISODE_SOURCE_MAP[source])


class GraphitiAudienceStore:
    """Sync :class:`IAudienceStore` adapter over async ``graphiti-core``.

    Lazy-init: the Graphiti client is constructed on first method call
    (not at ``__init__``) so a misconfigured Neo4j only surfaces when
    the seam is actually exercised. Construction parameters are stashed
    on ``self`` and consumed in :meth:`_ensure_client`.
    """

    def __init__(
        self,
        neo4j_uri: str,
        neo4j_user: str,
        neo4j_password: str,
        *,
        llm_base_url: str,
        llm_api_key: str,
        llm_model: Optional[str] = None,
        embedding_model: Optional[str] = None,
        embedding_dim: Optional[int] = None,
        reranking_model: Optional[str] = None,
    ) -> None:
        """Stash connection params; defer Graphiti construction to first use.

        ``llm_base_url`` / ``llm_api_key`` flow into Graphiti's
        :class:`OpenAIClient` so any **non-OpenAI-Cloud** OpenAI-compatible
        endpoint (local Ollama, LM Studio, a corp proxy, an Anthropic
        gateway with an OpenAI-shaped facade) drives entity extraction
        during ``add_episode``. The local-first posture means the
        simulator runs end-to-end with no cloud calls beyond this LLM
        endpoint.

        Local-first failure-closed: any URL whose hostname resolves to
        ``api.openai.com`` (regardless of scheme, port, path -- ``/v1``,
        ``/v1/``, schemeless, mixed case all refused) is rejected at
        construction time via :func:`llm_endpoint_is_openai_cloud`. The
        same check runs in the factory (defense-in-depth) but moving it
        here means direct constructor callers (integration tests,
        custom embedders) cannot silently route prompts to the cloud
        while a user thinks they're running local. There is intentionally
        no cloud opt-in path through this constructor; a user who needs
        OpenAI cloud must use a corp-proxy URL that exposes the OpenAI
        API under a different hostname.
        """
        if llm_endpoint_is_openai_cloud(llm_base_url):
            # llm_base_url may carry a query-string secret on a corp
            # proxy ("?key=..."); sanitise before quoting in the error.
            raise GraphitiInitError(
                "GraphitiAudienceStore requires an explicit local LLM "
                "endpoint (e.g. Ollama / LM Studio). Refused because "
                f"llm_base_url={_sanitize_uri(llm_base_url)!r} resolves to "
                "OpenAI cloud (or is empty, which falls through to the "
                "cloud default). Pass llm_base_url='http://localhost:11434/v1' "
                "for a local Ollama, or use a non-OpenAI corp proxy URL."
            )
        self._neo4j_uri = neo4j_uri
        self._neo4j_user = neo4j_user
        self._neo4j_password = neo4j_password
        self._llm_base_url = llm_base_url
        self._llm_api_key = llm_api_key
        # Model-name overrides for the underlying chat / embedding /
        # reranker calls. ``None`` falls back to upstream Graphiti's
        # OpenAI-cloud defaults (`gpt-4o` / `text-embedding-3-small`),
        # which only work when the operator's local server happens to
        # serve those exact model names. A real local deployment
        # (Ollama serving `qwen2.5:7b` + `nomic-embed-text`) MUST set
        # these env-driven overrides at the factory boundary.
        self._llm_model: Optional[str] = llm_model
        self._embedding_model: Optional[str] = embedding_model
        self._embedding_dim: Optional[int] = embedding_dim
        self._reranking_model: Optional[str] = reranking_model
        # Populated on first :meth:`_ensure_client` call.
        self._client: Any = None
        # Schema bootstrap (build_indices_and_constraints) is idempotent
        # but must run exactly once per process; the flag lets us call
        # ``_ensure_client`` from sync entry points without re-pinging
        # Neo4j on every call.
        self._schema_built: bool = False
        # set_ontology stores per-graph ontology so add_episode can pass
        # the matching entity_types kwarg into graphiti's add_episode.
        # Eager init (rather than lazy ``hasattr`` check) so add_episode
        # can read it unconditionally and pyright sees a stable type.
        self._ontologies: Dict[str, Ontology] = {}

    # ------------------------------------------------------------------
    # Async-to-sync bridge + lazy client init
    # ------------------------------------------------------------------

    def _run(self, coro: Coroutine[Any, Any, T]) -> T:
        """Drive an async Graphiti coroutine on a private event loop.

        We deliberately spin a fresh loop per call rather than caching
        one: the Flask request thread that calls into the seam does
        NOT own a running loop, and stashing a long-lived loop on
        ``self`` would make the store unsafe to share across gunicorn
        workers. For Graphiti's per-call workload (one ingest or one
        search) the loop-creation cost is dwarfed by Neo4j + LLM
        round-trips.

        Two safety primitives wrap the bridge:

          * **Concurrency cap** -- a module-level Semaphore caps
            in-flight ``_run`` calls at
            :data:`_GRAPHITI_MAX_CONCURRENT_CALLS` (overridable via
            ``GRAPHITI_MAX_CONCURRENT_CALLS``). Prevents N parallel
            Flask requests each spinning a loop + Neo4j round-trip
            and overwhelming the backend.
          * **Per-call timeout** -- wraps the coroutine in
            :func:`asyncio.wait_for` with a
            :data:`_GRAPHITI_CALL_TIMEOUT_S` ceiling
            (overridable via ``GRAPHITI_CALL_TIMEOUT_SEC``). A
            stalled Neo4j or LLM call surfaces as
            :class:`asyncio.TimeoutError` rather than wedging the
            request thread indefinitely. Defaults to 60s -- well
            above any healthy ingest / search round-trip.
        """
        with _GRAPHITI_CALL_SEMAPHORE:
            loop = asyncio.new_event_loop()
            try:
                return loop.run_until_complete(
                    asyncio.wait_for(coro, timeout=_GRAPHITI_CALL_TIMEOUT_S)
                )
            finally:
                loop.close()

    def _ensure_client(self) -> Any:
        """Lazily construct + connect the Graphiti client.

        Split into two phases so this method is safe to call from a SYNC
        entry point only:

        1. Object construction (imports + ``Graphiti(...)`` ctor): pure
           CPU, no I/O, idempotent. Cached on ``self._client``.
        2. Schema bootstrap (``build_indices_and_constraints``): async,
           hits Neo4j. Driven through :meth:`_run` which spins a private
           loop -- callers MUST be in sync context (which all
           ``IAudienceStore`` Protocol methods are by construction).

        The previous shape called ``_run(build_indices)`` from inside
        ``_cypher`` -- itself running inside ``_run(_cypher)`` -- which
        deadlocks on the outer loop ("This event loop is already
        running"). The fix is to make ``_cypher`` assume the client is
        already initialised and require every public sync method to
        invoke ``_ensure_client`` BEFORE entering its async body.

        Any failure mode (graphiti-core not installed, Neo4j unreachable,
        auth wrong, schema-init failed) re-raises as
        :class:`GraphitiInitError` with the offending ``NEO4J_URI`` in
        the message.
        """
        try:
            if self._client is None:
                graphiti_cls = _import_graphiti_symbol("graphiti_core", "Graphiti")
                llm_config_cls = _import_graphiti_symbol(
                    "graphiti_core.llm_client.config", "LLMConfig"
                )
                openai_client_cls = _import_graphiti_symbol(
                    "graphiti_core.llm_client.openai_client", "OpenAIClient"
                )
                # Local-first embedder + cross-encoder wiring. Without
                # these explicit kwargs upstream Graphiti defaults
                # ``embedder`` to a cloud-OpenAI embedder and
                # ``cross_encoder`` to a cloud-OpenAI reranker -- a
                # silent local-first contract violation. We wire both
                # against the same OPENAI-compatible base_url + api_key
                # the LLM client already uses so an Ollama / LM Studio
                # deployment handles embed/rerank too.
                #
                # Model NAMES (chat / embedding / reranker) come from
                # constructor kwargs so an operator running a local
                # server can override the OpenAI-cloud defaults via
                # env vars at the route boundary. ``None`` falls back
                # to upstream's defaults, which only work against an
                # actual cloud endpoint -- a local deployment that
                # serves ``nomic-embed-text`` MUST set the embedding
                # model override or embed calls will 404.
                embedder_config_cls = _import_graphiti_symbol(
                    "graphiti_core.embedder.openai", "OpenAIEmbedderConfig"
                )
                embedder_cls = _import_graphiti_symbol(
                    "graphiti_core.embedder.openai", "OpenAIEmbedder"
                )
                reranker_cls = _import_graphiti_symbol(
                    "graphiti_core.cross_encoder.openai_reranker_client",
                    "OpenAIRerankerClient",
                )

                llm_config_kwargs: Dict[str, Any] = {
                    "api_key": self._llm_api_key,
                    "base_url": self._llm_base_url,
                }
                if self._llm_model:
                    llm_config_kwargs["model"] = self._llm_model
                llm_config = llm_config_cls(**llm_config_kwargs)
                llm_client = openai_client_cls(config=llm_config)

                embedder_config_kwargs: Dict[str, Any] = {
                    "api_key": self._llm_api_key,
                    "base_url": self._llm_base_url,
                }
                if self._embedding_model:
                    embedder_config_kwargs["embedding_model"] = self._embedding_model
                if self._embedding_dim is not None:
                    embedder_config_kwargs["embedding_dim"] = self._embedding_dim
                embedder_config = embedder_config_cls(**embedder_config_kwargs)
                embedder = embedder_cls(config=embedder_config)

                # The reranker shares the LLM config (it issues chat
                # completions to score document/query pairs). Override
                # the model name via the reranker-specific env if the
                # operator wants a smaller / cheaper rerank model.
                if self._reranking_model:
                    reranker_config_kwargs = dict(llm_config_kwargs)
                    reranker_config_kwargs["model"] = self._reranking_model
                    reranker_config = llm_config_cls(**reranker_config_kwargs)
                else:
                    reranker_config = llm_config
                cross_encoder = reranker_cls(config=reranker_config)

                self._client = graphiti_cls(
                    uri=self._neo4j_uri,
                    user=self._neo4j_user,
                    password=self._neo4j_password,
                    llm_client=llm_client,
                    embedder=embedder,
                    cross_encoder=cross_encoder,
                )
            if not self._schema_built:
                # Idempotent on the Neo4j side; safe to retry on a fresh
                # container. Runs in its own loop via :meth:`_run`, so the
                # caller MUST be on a sync stack (no outer ``_run`` frame).
                self._run(self._client.build_indices_and_constraints())
                self._schema_built = True
            return self._client
        except Exception as exc:  # noqa: BLE001 -- re-raised as GraphitiInitError
            # Sanitise both the NEO4J_URI (which may carry
            # ``bolt://user:password@host``) and the exception text
            # (which may quote the same URI verbatim from the
            # driver). The exception class name is preserved so
            # operators have something to grep for.
            sanitised = _sanitize_uri(self._neo4j_uri)
            exc_class = type(exc).__name__
            raise GraphitiInitError(
                f"GraphitiAudienceStore could not initialise against "
                f"NEO4J_URI={sanitised!r}: {exc_class}"
            ) from exc

    # ------------------------------------------------------------------
    # Helpers: translate Graphiti node/edge dicts into our strict shapes
    # ------------------------------------------------------------------

    @staticmethod
    def _node_from_record(record: Any) -> EntityNode:
        """Reconstruct an :class:`EntityNode` from a Cypher record row.

        ``record`` is a ``neo4j.Record``-ish mapping with a single
        node-shaped value. We pull the properties dict off ``n`` and
        normalise: ``labels`` is a Cypher list, ``attributes`` is
        whatever extra JSON the node carries minus the well-known
        Graphiti fields we surface directly.
        """
        node: Any = record["n"]
        # neo4j-driver returns a Node object; props live on .items()
        # but we treat as Mapping for type sanity.
        props: Dict[str, Any] = dict(node.items()) if hasattr(node, "items") else dict(node)
        labels = list(getattr(node, "labels", []) or props.get("labels", []) or [])
        well_known = {"uuid", "name", "summary", "group_id"}
        attributes = {k: v for k, v in props.items() if k not in well_known}
        return EntityNode(
            uuid=str(props.get("uuid", "")),
            name=str(props.get("name", "")),
            labels=labels,
            summary=str(props.get("summary", "")),
            attributes=attributes,
        )

    @staticmethod
    def _edge_from_record(record: Any) -> EntityEdge:
        """Reconstruct an :class:`EntityEdge` from a Cypher row.

        Expects ``r`` (the edge), ``s.uuid`` (source uuid) and
        ``t.uuid`` (target uuid) in the row. Mirrors :meth:`_node_from_record`'s
        defensive coercions.
        """
        edge: Any = record["r"]
        props: Dict[str, Any] = dict(edge.items()) if hasattr(edge, "items") else dict(edge)
        well_known = {"uuid", "name", "fact", "source_node_uuid", "target_node_uuid"}
        attributes = {k: v for k, v in props.items() if k not in well_known}
        return EntityEdge(
            uuid=str(props.get("uuid", "")),
            name=str(props.get("name", "")),
            fact=str(props.get("fact", "")),
            source_node_uuid=str(record.get("source_uuid", props.get("source_node_uuid", ""))),
            target_node_uuid=str(record.get("target_uuid", props.get("target_node_uuid", ""))),
            attributes=attributes,
        )

    async def _cypher(
        self,
        query: str,
        params: Dict[str, Any],
    ) -> List[Any]:
        """Execute a Cypher query against Graphiti's underlying driver.

        Returns a list of record rows. Graphiti exposes its async Neo4j
        driver as ``graphiti.driver``; we use the driver's session API
        directly rather than reaching for a higher-level helper because
        the upstream library does not expose one for raw reads.

        Precondition: ``self._client`` must already be populated by a
        sync-stack ``_ensure_client`` call. Calling ``_ensure_client``
        from inside this coroutine would re-enter ``_run`` while the
        outer ``_run`` loop is still running, deadlocking on
        "this event loop is already running". Every public sync entry
        point that funnels through :meth:`_cypher` MUST invoke
        :meth:`_ensure_client` first.
        """
        if self._client is None:
            # Defensive: surfaces the contract violation loudly rather
            # than silently producing a NoneType-attr error mid-await.
            raise GraphitiInitError(
                "GraphitiAudienceStore._cypher called before "
                "_ensure_client; this is a programming error in the "
                "calling sync method (it must invoke _ensure_client "
                "before entering _run(self._cypher(...)))."
            )
        driver: Any = self._client.driver
        async with driver.session() as session:
            result: Any = await session.run(query, **params)
            records: List[Any] = []
            async for record in result:
                records.append(record)
            return records

    # ------------------------------------------------------------------
    # IAudienceStore -- ingest / mutation
    # ------------------------------------------------------------------

    def set_ontology(self, graph_id: str, ontology: Ontology) -> None:
        """Stash the ontology so subsequent ``add_episode`` calls type-extract.

        Graphiti's ``add_episode`` accepts a per-call ``entity_types``
        kwarg; there is no separate "set ontology" registration step on
        the Graphiti side. We therefore stash the ontology by ``graph_id``
        here and thread it into the ``add_episode`` kwargs in
        :meth:`add_episode`. Without this, Graphiti would fall back to
        its generic ``Entity`` extractor and the user-defined types in
        the supplied ``Ontology`` would be silently discarded.

        Touches the client to surface ``GraphitiInitError`` (Neo4j
        unreachable / auth wrong) at ontology-set time rather than
        deferring it to first ingest.
        """
        self._ensure_client()
        self._ontologies[graph_id] = ontology

    def add_episode(self, graph_id: str, episode: Episode) -> None:
        """Forward to ``graphiti.add_episode`` under the matching group_id.

        Graphiti's primitive is async; we drive it through :meth:`_run`.
        ``graph_id`` maps to Graphiti's ``group_id`` (the partition key
        Graphiti uses to scope nodes/edges across tenants).

        ``reference_time`` is REQUIRED by upstream Graphiti's
        ``add_episode``: some upstream versions raise when the kwarg
        is absent. To make ingestion robust against an absent
        caller-supplied timestamp we default to
        ``datetime.now(timezone.utc)`` when the caller does not
        supply one. Callers that DO supply a timestamp keep their
        value verbatim (ISO-8601 ``"Z"`` suffix is normalised to
        ``+00:00`` before ``datetime.fromisoformat`` parses it).

        If :meth:`set_ontology` was called for this ``graph_id``, its
        ``entity_types`` mapping flows into the underlying
        ``graphiti.add_episode(entity_types=...)`` call so the LLM
        extractor uses the user-defined types. Without this, the
        ontology would only be stored client-side and Graphiti would
        fall back to its generic ``Entity`` extractor -- silently
        dropping all custom types.
        """
        from datetime import datetime, timezone

        client = self._ensure_client()
        episode_type = _episode_type_for(episode.source)
        if episode.reference_time is not None:
            ref_time = datetime.fromisoformat(
                episode.reference_time.replace("Z", "+00:00")
            )
        else:
            ref_time = datetime.now(timezone.utc)
        kwargs: Dict[str, Any] = {
            "name": episode.name,
            "episode_body": episode.content,
            "source": episode_type,
            "source_description": episode.source_description,
            "group_id": graph_id,
            "reference_time": ref_time,
        }
        ontology: Optional[Ontology] = self._ontologies.get(graph_id)
        if ontology is not None and ontology.entity_types:
            # Upstream Graphiti expects ``entity_types`` as
            # ``dict[str, type[BaseModel]]`` -- the LLM extractor uses
            # the Pydantic class shape to drive structured extraction.
            # Our local ``Ontology.entity_types`` carries the wire-form
            # dict fragment (so the seam class stays import-light and
            # serialisable for tests). Convert at the boundary via
            # ``_entity_types_to_pydantic_classes`` so the upstream
            # extractor sees the shape it expects.
            kwargs["entity_types"] = _entity_types_to_pydantic_classes(
                ontology.entity_types,
            )
        self._run(client.add_episode(**kwargs))

    # ------------------------------------------------------------------
    # IAudienceStore -- query
    # ------------------------------------------------------------------

    def search(
        self,
        graph_id: str,
        query: str,
        *,
        limit: int = 10,
    ) -> SearchResults:
        """Hybrid search via ``graphiti.search``; result envelope re-shaped.

        Graphiti's ``search`` returns edge-shaped results (matched
        relations + their endpoints). For parity with
        :class:`MockZepStorage.search` -- which returns BOTH nodes and
        edges -- we also resolve each matched edge's source/target uuids
        back to their entity nodes via a single follow-up Cypher query.
        Per the docstring on :class:`SearchResults` we drop per-result
        scores because the downstream consumer treats the list as
        already-ranked.
        """
        client = self._ensure_client()
        raw: Any = self._run(
            client.search(query=query, group_ids=[graph_id], num_results=limit)
        )
        edges: List[EntityEdge] = []
        node_uuids: List[str] = []
        seen_uuids: set[str] = set()
        for item in (raw or [])[:limit]:
            src_uuid = str(getattr(item, "source_node_uuid", ""))
            dst_uuid = str(getattr(item, "target_node_uuid", ""))
            edges.append(
                EntityEdge(
                    uuid=str(getattr(item, "uuid", "")),
                    name=str(getattr(item, "name", "")),
                    fact=str(getattr(item, "fact", "")),
                    source_node_uuid=src_uuid,
                    target_node_uuid=dst_uuid,
                    attributes={},
                )
            )
            # Preserve first-seen order so rank from graphiti.search
            # carries through onto the nodes list (MockZep also ranks
            # nodes; parity requires we don't sort by uuid here).
            for uuid in (src_uuid, dst_uuid):
                if uuid and uuid not in seen_uuids:
                    seen_uuids.add(uuid)
                    node_uuids.append(uuid)

        nodes: List[EntityNode] = []
        if node_uuids:
            # One Cypher round-trip resolves every matched endpoint to a
            # full EntityNode. Filter by group_id so a poisoned edge
            # cannot leak nodes from a sibling graph.
            records = self._run(
                self._cypher(
                    "MATCH (n:Entity) WHERE n.group_id = $gid "
                    "AND n.uuid IN $uuids RETURN n",
                    {"gid": graph_id, "uuids": node_uuids},
                )
            )
            by_uuid: Dict[str, EntityNode] = {}
            for r in records:
                node = self._node_from_record(r)
                by_uuid[node.uuid] = node
            # Re-emit in graphiti.search rank order; drop any uuid that
            # didn't resolve (deleted between search and the read).
            nodes = [by_uuid[u] for u in node_uuids if u in by_uuid]
        return SearchResults(query=query, nodes=nodes, edges=edges)

    def get_all_nodes(self, graph_id: str) -> List[EntityNode]:
        """Raw Cypher dump of every ``:Entity`` node in ``group_id=graph_id``.

        Calls ``_ensure_client`` on the sync stack BEFORE entering
        ``_run(self._cypher(...))`` -- the async ``_cypher`` may not
        re-enter ``_ensure_client`` because that would call
        ``_run(build_indices_and_constraints)`` while the outer loop
        is still running, which deadlocks.
        """
        self._ensure_client()
        records = self._run(
            self._cypher(
                "MATCH (n:Entity) WHERE n.group_id = $gid RETURN n",
                {"gid": graph_id},
            )
        )
        return [self._node_from_record(r) for r in records]

    def get_all_edges(self, graph_id: str) -> List[EntityEdge]:
        """Raw Cypher dump of every entity-to-entity edge in ``group_id=graph_id``.

        See :meth:`get_all_nodes` for why ``_ensure_client`` runs on the
        sync stack BEFORE the ``_run(self._cypher(...))`` call.
        """
        self._ensure_client()
        records = self._run(
            self._cypher(
                "MATCH (s:Entity)-[r:RELATES_TO]->(t:Entity) "
                "WHERE r.group_id = $gid "
                "RETURN r, s.uuid AS source_uuid, t.uuid AS target_uuid",
                {"gid": graph_id},
            )
        )
        return [self._edge_from_record(r) for r in records]

    # ------------------------------------------------------------------
    # IAudienceStore -- original 2-method read surface
    # ------------------------------------------------------------------

    def filter_defined_entities(
        self,
        graph_id: str,
        defined_entity_types: List[str],
        *,
        enrich_with_edges: bool = False,
    ) -> FilteredEntities:
        """Cypher-backed equivalent of ``ZepEntityReader.filter_defined_entities``.

        Issues two queries: one for the global total (denominator) and
        one filtered to ``defined_entity_types``. An empty
        ``defined_entity_types`` list short-circuits to "no types
        requested -> empty filtered result" rather than "match
        everything" -- mirrors :class:`MockZepStorage`'s behaviour so
        the two backends agree on edge cases.
        """
        _ = enrich_with_edges  # accepted for ZepEntityReader parity
        # See :meth:`get_all_nodes` for the sync-stack rationale.
        self._ensure_client()
        total_records = self._run(
            self._cypher(
                "MATCH (n:Entity) WHERE n.group_id = $gid RETURN count(n) AS c",
                {"gid": graph_id},
            )
        )
        total_count = int(total_records[0]["c"]) if total_records else 0

        if not defined_entity_types:
            return FilteredEntities(
                entities=[],
                entity_types=set(),
                total_count=total_count,
                filtered_count=0,
            )

        records = self._run(
            self._cypher(
                "MATCH (n:Entity) WHERE n.group_id = $gid "
                "AND any(lbl IN labels(n) WHERE lbl IN $types) "
                "RETURN n",
                {"gid": graph_id, "types": list(defined_entity_types)},
            )
        )
        entities = [self._node_from_record(r) for r in records]
        types_found = {t for e in entities for t in e.labels if t in set(defined_entity_types)}
        return FilteredEntities(
            entities=entities,
            entity_types=types_found,
            total_count=total_count,
            filtered_count=len(entities),
        )

    def get_entities_by_type(
        self,
        graph_id: str,
        entity_type: str,
        *,
        enrich_with_edges: bool = False,
    ) -> List[EntityNode]:
        """Single-label filter, ordered by uuid for stable iteration."""
        _ = enrich_with_edges  # accepted for ZepEntityReader parity
        # See :meth:`get_all_nodes` for the sync-stack rationale.
        self._ensure_client()
        records = self._run(
            self._cypher(
                "MATCH (n:Entity) WHERE n.group_id = $gid "
                "AND $type IN labels(n) "
                "RETURN n ORDER BY n.uuid",
                {"gid": graph_id, "type": entity_type},
            )
        )
        return [self._node_from_record(r) for r in records]
