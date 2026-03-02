# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| `total_blocks` | `task.total_blocks` | `1` | `W2087530658` | Movie segment presented continuously during one acquisition run. | `inferred` | Single block keeps trigger scope simple for EEG logging. |
| `trial_per_block` | `task.trial_per_block` | `2` (human), `1` (qa/sim) | `W2809658419` | Naturalistic protocol emphasizes stable continuous viewing rather than many rapid trials. | `inferred` | QA/sim reduced for smoke validation only. |
| `conditions` | `task.conditions` | `['movie']` | `W2087530658` | Protocol is passive viewing of movie stimulus without condition switching. | `reference_exact` | No participant-visible condition labels. |
| `key_list` | `task.key_list` | `['space']` | `W2809658419` | Interaction is start/continue control, not in-movie decision behavior. | `inferred` | Used for instruction/goodbye progression only. |
| `pre_movie_fixation_duration` | `timing.pre_movie_fixation_duration` | `0.05` | `W2120149217` | Continuous EEG movie paradigms typically include short pre-onset stabilization period. | `inferred` | Short duration in this repo is optimized for QA/sim speed. |
| `movie_lead_in_duration` | `timing.movie_lead_in_duration` | `0.05` | `W2120149217` | Brief pre-playback lead-in before the main continuous stream. | `inferred` | Kept separate from fixation for stage-specific triggering. |
| `movie_duration` | `timing.movie_duration` | `4.0` (human), `2.0` (qa/sim) | `W2087530658` | Continuous movie window is the primary analysis segment. | `inferred` | QA/sim shortened to reduce runtime cost. |
| `movie_onset` | `triggers.map.movie_onset` | `1` | `W2120149217` | Event markers align EEG timeline with continuous audiovisual onset. | `inferred` | Trigger semantics are phase-aligned, not behavior-correctness aligned. |
| `movie_offset` | `triggers.map.movie_offset` | `2` | `W2120149217` | Continuous segment offset marker supports epoch extraction and synchronization. | `inferred` | Emitted as timeout trigger at playback end. |
