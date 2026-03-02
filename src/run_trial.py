from functools import partial

from psyflow import StimUnit, set_trial_context, next_trial_id

# trial stages use task-specific phase labels via set_trial_context(...)

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
    trial_id = next_trial_id()
    condition_id = str(condition)
    trial_data = {"condition": condition_id}
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    # phase: pre_movie_fixation
    pre_movie_fixation_unit = make_unit(unit_label="pre_movie_fixation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        pre_movie_fixation_unit,
        trial_id=trial_id,
        phase="pre_movie_fixation",
        deadline_s=getattr(settings, "pre_movie_fixation_duration", 0.0),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "pre_movie_fixation", "block_idx": block_idx},
        stim_id="fixation",
    )
    pre_movie_fixation_unit.show(duration=getattr(settings, "pre_movie_fixation_duration", 0.0)).to_dict(trial_data)

    # phase: movie_lead_in
    movie_lead_in_unit = make_unit(unit_label="movie_lead_in").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        movie_lead_in_unit,
        trial_id=trial_id,
        phase="movie_lead_in",
        deadline_s=getattr(settings, "movie_lead_in_duration", 0.0),
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "movie_lead_in", "block_idx": block_idx},
        stim_id="fixation",
    )
    movie_lead_in_unit.show(duration=getattr(settings, "movie_lead_in_duration", 0.0)).to_dict(trial_data)

    # phase: movie_playback
    movie_unit = make_unit(unit_label="movie").add_stim(stim_bank.get("movie"))
    set_trial_context(
        movie_unit,
        trial_id=trial_id,
        phase="movie_playback",
        deadline_s=settings.movie_duration,
        valid_keys=[],
        block_id=block_id,
        condition_id=condition_id,
        task_factors={"condition": condition_id, "stage": "movie_playback", "block_idx": block_idx},
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
    return trial_data
