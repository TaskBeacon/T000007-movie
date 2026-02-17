# CHANGELOG

All notable development changes for T000007-movie are documented here.

## [1.1.0] - 2026-02-17

### Added
- Added mode-aware `main.py` flow for human/qa/sim execution.
- Added split runtime configs:
  - `config/config.yaml`
  - `config/config_qa.yaml`
  - `config/config_scripted_sim.yaml`
  - `config/config_sampler_sim.yaml`
- Added task-local responder scaffold:
  - `responders/__init__.py`
  - `responders/README.md`
  - `responders/task_sampler.py`
- Added `outputs/.gitkeep` and standardized output folder handling.
- Added `assets/README.md` with placeholder media and replacement guidance.

### Changed
- Refactored `src/run_trial.py` to include `set_trial_context(...)` and simulation-compatible response window handling.
- Preserved passive movie logic while adding standardized stage bookkeeping.
- Upgraded trigger config to structured schema (`triggers.map/driver/policy/timing`).
- Updated `taskbeacon.yaml` to declare contract adoption (`contracts.psyflow_taps: v0.1.0`).
- Updated `.gitignore` for standardized outputs and generated artifacts.
- Updated `README.md` metadata and runtime/config usage.

### Fixed
- Aligned task config with framework contract requirements (`task.key_list` non-empty, structured triggers).

### Verified
- `psyflow-validate <task>` passes contract checks.
- `psyflow-qa <task> --config config/config_qa.yaml --no-maturity-update` passes.
- `python main.py sim --config config/config_scripted_sim.yaml` runs and writes sim artifacts.
