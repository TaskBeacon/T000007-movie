# Movie Assets

## Copyright Notice

The original movie stimulus is **not distributed** in this repository.
A placeholder movie file is included only for QA/sim/contract validation.

## Placeholder File

- `placeholder_movie.mp4`: local synthetic clip used to keep CI/QA runnable.

## Replacing with Licensed Movie

1. Put your licensed movie file in this folder.
2. Update `config/config.yaml` and sim/qa configs as needed:
   - `stimuli.movie.filename`
   - `timing.movie_duration`
3. Keep the same visual size settings unless you intentionally change protocol.
4. Re-run:
   - `psyflow-validate T000007-movie`
   - `psyflow-qa T000007-movie --config config/config_qa.yaml --no-maturity-update`

## Important

Do not use placeholder media for production data collection.
