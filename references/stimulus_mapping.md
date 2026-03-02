# Stimulus Mapping

## Mapping Table

| Condition | Stage/Phase | Stimulus IDs | Participant-Facing Content | Source Paper ID | Evidence (quote/figure/table) | Implementation Mode | Asset References | Notes |
|---|---|---|---|---|---|---|---|---|
| `movie` | `pre_movie_fixation` | `fixation` | White `+` fixation centered on black background before playback. | `W2087530658` | Naturalistic movie viewing protocols include pre-stimulus stabilization baseline. | `psychopy_builtin` | `config/config*.yaml -> stimuli.fixation` | No response required in this phase. |
| `movie` | `movie_lead_in` | `fixation` | Same centered fixation during brief lead-in before movie onset. | `W2120149217` | Continuous EEG engagement paradigms separate pre-onset window from primary clip period. | `psychopy_builtin` | `config/config*.yaml -> stimuli.fixation` | Maintains gaze centering before movie onset trigger. |
| `movie` | `movie_playback` | `movie` | Continuous movie clip presented at center; participant watches passively. | `W2087530658` | Core task operation is passive viewing under continuous recording. | `licensed_external_asset` | `assets/demo_movie.mp4` (replace with licensed clip) | No trial-level choice or accuracy response is collected. |

