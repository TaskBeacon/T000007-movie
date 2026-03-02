# Task Logic Audit

## 1. Paradigm Intent

- Task: Passive naturalistic movie viewing task for EEG timing-aligned acquisition.
- Primary construct: Ongoing neural synchronization/engagement during continuous audiovisual stimulation.
- Manipulated factors: None in baseline profile (single `movie` condition).
- Dependent measures: Time-locked EEG/trigger traces and optional derived engagement metrics.
- Key citations:
  - W2087530658
  - W2120149217
  - W2809658419

## 2. Block/Trial Workflow

### Block Structure

- Total blocks: 1.
- Trials per block: Human profile uses 2; QA/sim profiles use 1 for fast validation.
- Randomization/counterbalancing: Not applicable for single-condition passive run.
- Condition weight policy:
  - `task.condition_weights` is not defined.
  - `TaskSettings.resolve_condition_weights()` is not used in this task.
  - Even/default generation applies because only one condition token exists.
- Condition generation method:
  - Built-in `BlockUnit.generate_conditions(order="sequential")`.
  - No custom generator is required because condition semantics are scalar (`movie`).
  - Generated condition data shape: scalar condition token (`"movie"`) passed to `run_trial.py`.
- Runtime-generated trial values (if any):
  - No stochastic trial factors generated at runtime.
  - Determinism depends on fixed config and sequential condition generation.

### Trial State Machine

1. State name: `pre_movie_fixation`
   - Onset trigger: none (phase bookkeeping only)
   - Stimuli shown: centered fixation (`+`)
   - Valid keys: `task.key_list` (`space`) but no behavioral branch outcome is used
   - Timeout behavior: auto-advance after `timing.pre_movie_fixation_duration`
   - Next state: `movie_lead_in`
2. State name: `movie_lead_in`
   - Onset trigger: none (phase bookkeeping only)
   - Stimuli shown: centered fixation (`+`)
   - Valid keys: `task.key_list` (`space`) but no behavioral branch outcome is used
   - Timeout behavior: auto-advance after `timing.movie_lead_in_duration`
   - Next state: `movie_playback`
3. State name: `movie_playback`
   - Onset trigger: `triggers.map.movie_onset`
   - Stimuli shown: movie clip (`stimuli.movie`)
   - Valid keys: none (`[]`)
   - Timeout behavior: close at `timing.movie_duration`, emit `triggers.map.movie_offset`
   - Next state: trial end

## 3. Condition Semantics

- Condition ID: `movie`
- Participant-facing meaning: Passive viewing of a centered movie clip.
- Concrete stimulus realization (visual/audio):
  - fixation cross during pre-movie phases
  - movie file playback in the main phase
- Outcome rules: no correctness scoring and no reward update.

Participant-facing text/stimuli source:

- Participant-facing text source: `config/*.yaml` `stimuli` entries (`instruction_text`, `good_bye`, `fixation`, `movie`).
- Why this source is appropriate for auditability: language and visual content are centralized in config and traceable without code edits.
- Localization strategy: swap localized text/font in config profiles while preserving runtime logic in `run_trial.py`.

## 4. Response and Scoring Rules

- Response mapping: `space` is used only for instruction/block/goodbye continuation.
- Response key source: `task.key_list` in config.
- If code-defined, why config-driven mapping is not sufficient: not applicable.
- Missing-response policy: no in-trial response expected during movie playback.
- Correctness logic: none.
- Reward/penalty updates: none.
- Running metrics: none in baseline runtime.

## 5. Stimulus Layout Plan

- Screen name: `pre_movie_fixation`
- Stimulus IDs shown together: `fixation`
- Layout anchors (`pos`): center `(0, 0)`
- Size/spacing (`height`, width, wrap): defaults from text stim bank
- Readability/overlap checks: single stimulus; no overlap risk
- Rationale: center-gaze stabilization before movie onset

- Screen name: `movie_lead_in`
- Stimulus IDs shown together: `fixation`
- Layout anchors (`pos`): center `(0, 0)`
- Size/spacing (`height`, width, wrap): defaults from text stim bank
- Readability/overlap checks: single stimulus; no overlap risk
- Rationale: preserve gaze alignment at lead-in boundary

- Screen name: `movie_playback`
- Stimulus IDs shown together: `movie`
- Layout anchors (`pos`): center window anchor
- Size/spacing (`height`, width, wrap): configured movie size `[22.1, 12.4] deg`
- Readability/overlap checks: single asset; verify rendered frame fully visible in QA
- Rationale: controlled central presentation for time-locked naturalistic viewing

## 6. Trigger Plan

- `exp_onset` (`98`): experiment start marker.
- `block_onset` (`100`): block start marker.
- `movie_onset` (`1`): movie playback onset.
- `movie_offset` (`2`): movie playback timeout/offset.
- `block_end` (`101`): block end marker.
- `exp_end` (`99`): experiment end marker.

## 7. Architecture Decisions (Auditability)

- `main.py` runtime flow style: simple single mode-aware flow (`human|qa|sim`) with shared setup order.
- `utils.py` used?: no.
- Custom controller used?: no.
- Why PsyFlow-native path is sufficient: passive movie task is representable with standard `BlockUnit`, `StimBank`, `StimUnit`, and `set_trial_context`.
- Legacy/backward-compatibility fallback logic required?: no.

## 8. Inference Log

- Decision: Use very short pre-movie phases (`0.05s`) in default profiles.
- Why inference was required: papers emphasize continuous viewing but do not prescribe exact short lead-in durations for this implementation context.
- Citation-supported rationale: W2087530658 and W2120149217 support continuous movie-based acquisition with phase-aligned event timing.

- Decision: Keep single `movie` condition with no response scoring.
- Why inference was required: repository profile targets baseline passive viewing rather than condition-comparison variant.
- Citation-supported rationale: W2809658419 argues for real-world naturalistic paradigms where continuous stimulus exposure is primary.
