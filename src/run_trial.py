from functools import partial

from psyflow import StimUnit, set_trial_context

# trial stages in contract order: cue -> anticipation -> target -> feedback
_TRIAL_COUNTER = 0


def _next_trial_id() -> int:
    global _TRIAL_COUNTER
    _TRIAL_COUNTER += 1
    return _TRIAL_COUNTER


def _deadline_s(value) -> float | None:
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, (list, tuple)) and value:
        try:
            return float(max(value))
        except Exception:
            return None
    return None


def run_trial(
    win,
    kb,
    settings,
    condition,
    stim_bank,
    trigger_runtime=None,
    block_id=None,
    block_idx=None,
):
    """Run one movie presentation trial."""
    trial_id = _next_trial_id()
    condition_id = str(condition)
    trial_data = {"condition": condition_id}
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    # cue
    cue_unit = make_unit(unit_label="cue").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        cue_unit,
        trial_id=trial_id,
        phase="cue",
        deadline_s=_deadline_s(getattr(settings, "cue_duration", 0.0)),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "cue", "block_idx": block_idx},
        stim_id="fixation",
    )
    cue_unit.show(duration=getattr(settings, "cue_duration", 0.0)).to_dict(trial_data)

    # anticipation
    anticipation_unit = make_unit(unit_label="anticipation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        anticipation_unit,
        trial_id=trial_id,
        phase="anticipation",
        deadline_s=_deadline_s(getattr(settings, "anticipation_duration", 0.0)),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "anticipation", "block_idx": block_idx},
        stim_id="fixation",
    )
    anticipation_unit.show(duration=getattr(settings, "anticipation_duration", 0.0)).to_dict(trial_data)

    # target
    movie_unit = make_unit(unit_label="movie").add_stim(stim_bank.get("movie"))
    set_trial_context(
        movie_unit,
        trial_id=trial_id,
        phase="target",
        deadline_s=_deadline_s(settings.movie_duration),
        valid_keys=[],
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "movie", "block_idx": block_idx},
        stim_id="movie",
    )
    movie_unit.capture_response(
        keys=[],
        duration=settings.movie_duration,
        onset_trigger=settings.triggers.get("movie_onset"),
        timeout_trigger=settings.triggers.get("movie_offset"),
        terminate_on_response=False,
    )
    movie_unit.to_dict(trial_data)

    # feedback
    make_unit(unit_label="feedback").show(duration=0.0).to_dict(trial_data)
    return trial_data
