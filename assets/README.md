# Movie Assets

## Asset Policy

The repository includes a generated reference movie clip for open, reproducible
task execution. It avoids bundling restricted third-party movie material while
keeping the task runnable in human, QA, and simulation profiles.

## Reference File

- `reference_movie.mp4`: generated synthetic movie clip used by the default configs.

## Replacing With Study-Specific Movie Media

1. Put your approved movie file in this folder.
2. Update `config/config.yaml` and sim/qa configs as needed:
   - `stimuli.movie.filename`
   - `timing.movie_duration`
3. Keep the same visual size settings unless you intentionally change protocol.
4. Re-run:
   - `psyflow-validate T000007-movie`
   - `psyflow-qa T000007-movie --config config/config_qa.yaml --no-maturity-update`

## Important

If a study requires a specific copyrighted or licensed movie, replace the
reference clip and document the media source in `references/`.
