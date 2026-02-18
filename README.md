# Movie Watching Task

![Maturity: piloted](https://img.shields.io/badge/Maturity-piloted-16a34a?style=flat-square&labelColor=111827)

| Field | Value |
|---|---|
| Name | Movie Watching Task |
| Version | v1.1.0 |
| URL / Repository | https://github.com/TaskBeacon/T000007-movie |
| Short Description | Passive movie-viewing EEG task with centered movie stimulus |
| Created By | Zhipeng Cao (zhipeng30@foxmail.com) |
| Date Updated | 2026-02-17 |
| PsyFlow Version | 0.1.9 |
| PsychoPy Version | 2025.1.1 |
| Modality | Behavior/EEG |
| Language | Chinese |
| Voice Name | zh-CN-YunyangNeural |

## 1. Task Overview

This task presents a movie stimulus while participants watch passively.
No trial response is required during movie playback.

## 2. Task Flow

### Block-Level Flow

- Initialize runtime, triggers, and movie stimulus resources.
- Present instructions and execute configured movie trials/blocks.
- Save outputs and close PsychoPy runtime cleanly.

### Trial-Level Flow

- `pre_movie_fixation`: pre-playback fixation.
- `movie_lead_in`: short lead-in stage before playback.
- `movie_playback`: movie presentation window (passive viewing).

## Runtime Modes

- Human (default): `python main.py`
- QA: `python main.py qa --config config/config_qa.yaml`
- Scripted sim: `python main.py sim --config config/config_scripted_sim.yaml`
- Sampler sim: `python main.py sim --config config/config_sampler_sim.yaml`

## 3. Configuration Summary

- `config/config.yaml`: base human run profile
- `config/config_qa.yaml`: QA/dev profile
- `config/config_scripted_sim.yaml`: scripted simulation profile
- `config/config_sampler_sim.yaml`: sampler simulation profile

## Assets and Copyright Workaround

The original copyrighted movie clip is not included in this repository.
A placeholder movie file is included for QA/sim and pipeline validation.

See `assets/README.md` for:
- placeholder file policy
- how to replace with licensed movie media
- expected filename/path constraints

## Outputs

- Human: `outputs/human/`
- QA: `outputs/qa/`
- Scripted sim: `outputs/sim/`
- Sampler sim: `outputs/sim_sampler/`

## Task Notes

- Trigger config uses structured schema: `triggers.map/driver/policy/timing`.
- Trial responder context is wired in `src/run_trial.py` via `set_trial_context(...)`.
- Task-specific sampler is in `responders/task_sampler.py`.

### Runtime Context Phases
| Phase Label | Meaning |
|---|---|
| `pre_movie_fixation` | pre movie fixation stage in `src/run_trial.py` responder context. |
| `movie_lead_in` | movie lead in stage in `src/run_trial.py` responder context. |
| `movie_playback` | movie playback stage in `src/run_trial.py` responder context. |

## 4. Methods (for academic publication)

Participants passively view movie stimuli while event timing and trigger emissions are controlled for reproducible acquisition. Each trial includes fixation, lead-in, and playback stages without behavioral response requirements. The task is suitable for naturalistic viewing paradigms where synchronized presentation logs are required for downstream analysis.

