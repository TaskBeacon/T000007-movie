# Task Plot Audit

- generated_at: 2026-03-10T00:17:28
- mode: existing
- task_path: E:\Taskbeacon\T000007-movie

## 1. Inputs and provenance

- E:\Taskbeacon\T000007-movie\README.md
- E:\Taskbeacon\T000007-movie\config\config.yaml
- E:\Taskbeacon\T000007-movie\src\run_trial.py

## 2. Evidence extracted from README

- Trial-Level Flow table not found; run_trial.py used as primary source.

## 3. Evidence extracted from config/source

- movie: phase=pre movie fixation, deadline_expr=getattr(settings, 'pre_movie_fixation_duration', 0.0), response_expr=n/a, stim_expr='fixation'
- movie: phase=movie lead in, deadline_expr=getattr(settings, 'movie_lead_in_duration', 0.0), response_expr=n/a, stim_expr='fixation'
- movie: phase=movie playback, deadline_expr=settings.movie_duration, response_expr=settings.movie_duration, stim_expr='movie'

## 4. Mapping to task_plot_spec

- timeline collection: one representative timeline per unique trial logic
- phase flow inferred from run_trial set_trial_context order and branch predicates
- participant-visible show() phases without set_trial_context are inferred where possible and warned
- duration/response inferred from deadline/capture expressions
- stimulus examples inferred from stim_id + config stimuli
- conditions with equivalent phase/timing logic collapsed and annotated as variants
- root_key: task_plot_spec
- spec_version: 0.2

## 5. Style decision and rationale

- Single timeline-collection view selected by policy: one representative condition per unique timeline logic.

## 6. Rendering parameters and constraints

- output_file: task_flow.png
- dpi: 300
- max_conditions: 4
- screens_per_timeline: 6
- screen_overlap_ratio: 0.1
- screen_slope: 0.08
- screen_slope_deg: 25.0
- screen_aspect_ratio: 1.4545454545454546
- qa_mode: local
- auto_layout_feedback:
  - layout pass 1: crop-only; left=0.043, right=0.043, blank=0.156
- auto_layout_feedback_records:
  - pass: 1
    metrics: {'left_ratio': 0.0427, 'right_ratio': 0.0427, 'blank_ratio': 0.1564}

## 7. Output files and checksums

- E:\Taskbeacon\T000007-movie\references\task_plot_spec.yaml: sha256=5ee394f6b99921d5e9b2d0cecf213f2853f4b2412db1c6562ce1a72e39fdabbf
- E:\Taskbeacon\T000007-movie\references\task_plot_spec.json: sha256=459dd99c789d3be7190184fcda874a6f40e9cad370b51c5858bb88c903c2abbd
- E:\Taskbeacon\T000007-movie\references\task_plot_source_excerpt.md: sha256=60b599a46eb45a7472b52a8bdadc56997c88631ba69cd1aafeab05f1ce484188
- E:\Taskbeacon\T000007-movie\task_flow.png: sha256=d388d09a4fcc8450933f1c40e375d84dee6a500039790d483fa1fc558d36cb7c

## 8. Inferred/uncertain items

- movie:pre movie fixation:heuristic numeric parse from 'getattr(settings, 'pre_movie_fixation_duration', 0.0)'
- movie:movie lead in:heuristic numeric parse from 'getattr(settings, 'movie_lead_in_duration', 0.0)'
