from psyflow import BlockUnit,StimBank, StimUnit,SubInfo,TaskSettings,initialize_triggers
from psyflow import load_config,count_down, initialize_exp
import pandas as pd
from psychopy import core
from src import run_trial




# 1. Load config
cfg = load_config()

# 2. Collect subject info
subform = SubInfo(cfg['subform_config'])
subject_data = subform.collect()

# 3. Load task settings
settings = TaskSettings.from_dict(cfg['task_config'])
settings.add_subinfo(subject_data)

# 4. setup triggers
settings.triggers = cfg['trigger_config']
trigger_runtime = initialize_triggers(cfg)

# 5. Set up window & input
win, kb = initialize_exp(settings)
# 6. Setup stimulus bank
stim_bank = StimBank(win,cfg['stim_config'])\
    .convert_to_voice(['instruction_text','good_bye'], voice=settings.voice_name)\
    .preload_all()
# stim_bank.preview_all() 
settings.save_to_json() # save all settings to json file

trigger_runtime.send(settings.triggers.get("exp_onset"))
StimUnit('instruction',win,kb)\
    .add_stim(stim_bank.get('instruction_text'))\
    .add_stim(stim_bank.get('instruction_text_voice'))\
    .wait_and_continue()
count_down(win, 3)

block = BlockUnit(
        block_id=f"block_0",
        block_idx=0,
        settings=settings,
        window=win,
        keyboard=kb
    ).generate_conditions()\
    .on_start(lambda b: trigger_runtime.send(settings.triggers.get("block_onset")))\
    .on_end(lambda b: trigger_runtime.send(settings.triggers.get("block_end")))\
    .run_trial(func=run_trial, stim_bank=stim_bank, trigger_runtime=trigger_runtime)


StimUnit('goodbye',win,kb)\
    .add_stim(stim_bank.get('good_bye'))\
    .add_stim(stim_bank.get('good_bye_voice'))\
    .wait_and_continue(terminate=True)
trigger_runtime.send(settings.triggers.get("exp_end"))
# 10. Close everything
trigger_runtime.close()
core.quit()


