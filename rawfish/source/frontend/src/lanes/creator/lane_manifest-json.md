---
title: "frontend/src/lanes/creator/lane_manifest.json"
noindex: true
---

```json
{
  "lane_id": "creator",
  "label": "Creator",
  "summary": "Stress-test how audience cohorts may react to a creator brief.",
  "accent": "#E64A19",
  "default_provider": {
    "mode": "local_ollama",
    "model": "qwen3-coder:30b"
  },
  "cockpit_slots": [
    "statistical_workbench_inline_editor",
    "statistical_workbench_override_badge",
    "statistical_workbench_provenance_chip",
    "statistical_workbench_validity_strip",
    "statistical_workbench_variant_strip",
    "statistical_workbench_impact_tooltip",
    "statistical_workbench_preflight_meter",
    "statistical_workbench_drift_subpanel",
    "statistical_workbench_salt_seed_panel",
    "statistical_workbench_priors_attach_panel",
    "statistical_workbench_active_hours_grid",
    "statistical_workbench_manifest_chip"
  ],
  "cohorts": [
    { "id": "fans", "label": "Long-time fans", "short_label": "FAN", "color": "#E64A19" },
    { "id": "skeptics", "label": "Gen-Z skeptics", "short_label": "GENZ", "color": "#2563EB" },
    { "id": "casual", "label": "Casual viewers", "short_label": "CAS", "color": "#059669" }
  ],
  "run_timeline_platforms": [
    { "id": "plaza", "label": "INFO PLAZA", "accent": "#E64A19" },
    { "id": "community", "label": "COMMUNITY", "accent": "#2563EB" }
  ],
  "report_sections": [
    { "id": "reaction_map", "label": "Reaction map" },
    { "id": "cohort_tensions", "label": "Cohort tensions" },
    { "id": "open_questions", "label": "Open questions" }
  ],
  "analysis_panels": {
    "compare": { "enabled": true },
    "counterfactual": { "enabled": false },
    "sensitivity": { "enabled": false }
  },
  "eval_instruments": {
    "cost_preflight": {
      "default_ensemble_n": 5,
      "default_rounds": 16,
      "budget_cap": 500,
      "provider_modes": ["local_ollama", "local_openai_compatible", "external"],
      "provider_selection_scope": "per_run",
      "external_budget": { "currency": "USD", "warn_at": 1.0 }
    }
  }
}
```
