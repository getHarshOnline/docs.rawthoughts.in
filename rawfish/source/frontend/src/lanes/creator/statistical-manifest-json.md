---
title: "frontend/src/lanes/creator/statistical.manifest.json"
noindex: true
---

```json
{
  "lane_id": "creator",
  "version": "0.1",
  "impact_model": {
    "source": "runSurrogateExplainer",
    "fallback": "no impact preview available"
  },
  "citation_policy": {
    "required": true,
    "table": "creator_statistical_v0"
  },
  "provenance_policy": {
    "allowed": [
      "user-set",
      "manifest-default",
      "inferred-from-prior",
      "sampled",
      "inferred-from-parseScenario"
    ]
  },
  "fields": [
    {
      "id": "run.run_seed",
      "label": "Run seed",
      "kind": "integer",
      "control": "numeric",
      "default": 1729,
      "min": 0,
      "max": 2147483647,
      "step": 1,
      "description": "Master seed for deterministic audience response sampling.",
      "why_it_matters": "Controls deterministic replay and persona sampling without changing the scenario.",
      "citation_key": "run_controls.run_seed",
      "modalities": [
        "numeric"
      ],
      "validation": [
        {
          "rule_id": "integer_in_range",
          "args": {
            "min": 0
          }
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "sampling",
        "comparison"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "run.ensemble_n",
      "label": "Ensemble size",
      "kind": "integer",
      "control": "slider_number",
      "default": 5,
      "min": 1,
      "max": 40,
      "step": 1,
      "description": "Number of independent audience response passes to run.",
      "why_it_matters": "Moves the scale guard, token estimate, and stability of aggregate findings.",
      "citation_key": "scale_guard.ensemble_n",
      "modalities": [
        "slider",
        "numeric"
      ],
      "validation": [
        {
          "rule_id": "integer_in_range",
          "args": {
            "min": 1,
            "max": 40
          }
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "sampling",
        "run-behavior",
        "comparison"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "run.drift_horizon_rounds",
      "label": "Conversation rounds",
      "kind": "integer",
      "control": "slider_number",
      "default": 16,
      "min": 1,
      "max": 96,
      "step": 1,
      "description": "Maximum simulated interaction rounds per cohort.",
      "why_it_matters": "Longer runs expose slower audience tensions while increasing runtime and token cost.",
      "citation_key": "run_controls.drift_horizon_rounds",
      "modalities": [
        "slider",
        "numeric"
      ],
      "validation": [
        {
          "rule_id": "integer_in_range",
          "args": {
            "min": 1,
            "max": 96
          }
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "run-behavior",
        "comparison"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "cohort.activity_level",
      "label": "Activity level",
      "kind": "number",
      "control": "slider_number",
      "default": 0.5,
      "min": 0,
      "max": 1,
      "step": 0.05,
      "units": "%",
      "description": "Baseline probability that an audience cohort is active during a round.",
      "why_it_matters": "Raises or lowers cohort participation pressure before report claims are generated.",
      "citation_key": "agent_activity.activity_level",
      "modalities": [
        "slider",
        "numeric"
      ],
      "validation": [
        {
          "rule_id": "float_in_range",
          "args": {
            "min": 0,
            "max": 1
          }
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "sampling",
        "run-behavior"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "cohort.posts_per_hour",
      "label": "Posts per hour",
      "kind": "number",
      "control": "slider_number",
      "default": 1,
      "min": 0,
      "max": 4,
      "step": 0.1,
      "units": "/hour",
      "description": "Approximate outbound posting cadence for a cohort.",
      "why_it_matters": "Changes how much each cohort can inject into the simulated conversation.",
      "citation_key": "agent_activity.posts_per_hour",
      "modalities": [
        "slider",
        "numeric"
      ],
      "validation": [
        {
          "rule_id": "float_in_range",
          "args": {
            "min": 0,
            "max": 4
          }
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "run-behavior"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "cohort.comments_per_hour",
      "label": "Comments per hour",
      "kind": "number",
      "control": "slider_number",
      "default": 2,
      "min": 0,
      "max": 8,
      "step": 0.1,
      "units": "/hour",
      "description": "Approximate reply/comment cadence for a cohort.",
      "why_it_matters": "Changes how strongly a cohort reacts to other agents rather than posting alone.",
      "citation_key": "agent_activity.comments_per_hour",
      "modalities": [
        "slider",
        "numeric"
      ],
      "validation": [
        {
          "rule_id": "float_in_range",
          "args": {
            "min": 0,
            "max": 8
          }
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "run-behavior"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "cohort.influence_weight",
      "label": "Influence weight",
      "kind": "number",
      "control": "slider_number",
      "default": 1,
      "min": 0,
      "max": 3,
      "step": 0.05,
      "description": "Relative graph and reaction weight for the cohort.",
      "why_it_matters": "Influence affects which cohort reactions dominate aggregate report summaries.",
      "citation_key": "agent_activity.influence_weight",
      "modalities": [
        "slider",
        "numeric"
      ],
      "validation": [
        {
          "rule_id": "float_in_range",
          "args": {
            "min": 0,
            "max": 3
          }
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "run-behavior",
        "report-weighting"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "cohort.sentiment_bias",
      "label": "Sentiment bias",
      "kind": "number",
      "control": "slider_number",
      "default": 0,
      "min": -1,
      "max": 1,
      "step": 0.05,
      "description": "Starting sentiment offset for the cohort.",
      "why_it_matters": "Makes explicit whether a cohort starts receptive, neutral, or skeptical.",
      "citation_key": "agent_activity.sentiment_bias",
      "modalities": [
        "slider",
        "numeric"
      ],
      "validation": [
        {
          "rule_id": "float_in_range",
          "args": {
            "min": -1,
            "max": 1
          }
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "run-behavior",
        "report-weighting"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "cohort.active_hours",
      "label": "Active hours",
      "kind": "active_hours",
      "control": "active_hours_grid",
      "default": [
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21
      ],
      "description": "Local hours during which audience agents can react.",
      "why_it_matters": "Constrains timing patterns without fabricating engagement.",
      "citation_key": "agent_activity.active_hours",
      "modalities": [
        "grid24h",
        "preset_picker"
      ],
      "validation": [
        {
          "rule_id": "hours_0_23"
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "run-behavior"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "run.persona_salts",
      "label": "Cohort salts",
      "kind": "salt_map",
      "control": "key_value",
      "default": {
        "fans": "creator-default",
        "skeptics": "creator-default",
        "casual": "creator-default"
      },
      "description": "Optional deterministic salts for cohort-level variation.",
      "why_it_matters": "Keeps cohort identity stable when comparing base and reseeded variants.",
      "citation_key": "run_controls.persona_salts",
      "modalities": [
        "chip_select"
      ],
      "validation": [
        {
          "rule_id": "salt_map"
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "sampling",
        "comparison"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "sampled",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "cohort.priors.attached_priors_id",
      "label": "Prior bundle",
      "kind": "text",
      "control": "text",
      "default": "creator_default_priors_v0",
      "description": "Identifier for the creator-audience prior bundle applied to the run.",
      "why_it_matters": "Records assumptions used before generated audience reactions are observed.",
      "citation_key": "priors.bundle_id",
      "modalities": [
        "chip_select"
      ],
      "validation": [
        {
          "rule_id": "text_non_empty"
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "sampling",
        "report-weighting"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "inferred-from-prior"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "lock_supported": true
    },
    {
      "id": "manifest.claim_tag_allowlist",
      "label": "Claim tag allowlist",
      "kind": "multi_select",
      "control": "checkbox_group",
      "default": [
        "simulated_observation",
        "inference",
        "assumption",
        "requires_validation"
      ],
      "description": "Claim provenance tags the creator report is allowed to emit.",
      "why_it_matters": "Keeps report language honest about simulated versus assumed claims.",
      "citation_key": "hypothesis_tags.canonical",
      "modalities": [
        "chip_select"
      ],
      "validation": [
        {
          "rule_id": "enum_subset"
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "report-weighting"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default"
      ],
      "provenance_policy": {
        "initial": "manifest-default",
        "lock_default": true
      },
      "options": [
        {
          "value": "source_grounded",
          "label": "Source grounded"
        },
        {
          "value": "simulated_observation",
          "label": "Simulated observation"
        },
        {
          "value": "inference",
          "label": "Inference"
        },
        {
          "value": "assumption",
          "label": "Assumption"
        },
        {
          "value": "requires_validation",
          "label": "Requires validation"
        }
      ],
      "lock_supported": true
    },
    {
      "id": "variant.audience_metric_focus",
      "label": "Audience metric focus",
      "kind": "multi_select",
      "control": "checkbox_group",
      "default": [
        "engagement_risk",
        "confusion_risk"
      ],
      "description": "Creator-specific response dimensions to emphasize in analysis.",
      "why_it_matters": "Narrows summaries to the audience response signals the lane can substantiate.",
      "citation_key": "creator.report_metrics",
      "modalities": [
        "chip_select"
      ],
      "validation": [
        {
          "rule_id": "enum_subset"
        }
      ],
      "lane_applicability": [
        "creator"
      ],
      "affects": [
        "report-weighting",
        "comparison"
      ],
      "impact_hint": {
        "source": "runSurrogateExplainer",
        "swing_magnitude": null,
        "kernel_disclaimer": "static_kernel_v1; no impact preview available until sensitivity runs.",
        "cooccurrence_caveat": "co-occurrence, not causal"
      },
      "provenance": [
        "manifest-default",
        "user-set"
      ],
      "provenance_policy": {
        "initial": "manifest-default"
      },
      "options": [
        {
          "value": "engagement_risk",
          "label": "Engagement risk"
        },
        {
          "value": "confusion_risk",
          "label": "Confusion risk"
        },
        {
          "value": "backlash_risk",
          "label": "Backlash risk"
        },
        {
          "value": "loyalty_signal",
          "label": "Loyalty signal"
        }
      ],
      "lock_supported": true
    }
  ]
}
```
