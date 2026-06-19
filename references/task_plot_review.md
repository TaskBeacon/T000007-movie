# Task Plot Review

## Evidence Match

- Pass: task title and construct match the passive movie-viewing task.
- Pass: single Movie row matches the configured single `movie` condition.
- Pass: phase order matches `src/run_trial.py`: Pre-movie fixation -> Lead-in -> Movie playback.
- Pass: timing labels match `config/config.yaml`: 50 ms, 50 ms, and 4000 ms.
- Pass: movie playback is shown as passive viewing with no response keys.
- Pass: SPACE is identified as start/exit continuation only, not an in-movie response.

## Visual Quality

- Pass: timeline text is readable.
- Pass: generated content stays below the reserved header band.
- Pass: fixed title and Construct subtitle are centered and consistent with the new style.
- Pass: top-right TaskBeacon logo lockup is borderless and does not overlap content.
- Pass: no extra generated title, watermark, brand text, people, or lab-equipment scene is present.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the section embeds `![Task Flow](task_flow.png)`.
- Pass: final image is saved as `task_flow.png`; raw timeline is saved as `references/task_plot_timeline_raw.png`.
