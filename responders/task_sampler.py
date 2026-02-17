from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from psyflow.sim.contracts import Action, Observation, SessionInfo


@dataclass
class TaskSamplerResponder:
    continue_key: str = "space"
    rt_continue_s: float = 0.25

    def __post_init__(self) -> None:
        self._rng: Any = None
        self.rt_continue_s = max(0.01, float(self.rt_continue_s))

    def start_session(self, session: SessionInfo, rng: Any) -> None:
        self._rng = rng

    def on_feedback(self, fb: Any) -> None:
        return None

    def end_session(self) -> None:
        return None

    def act(self, obs: Observation) -> Action:
        valid_keys = list(obs.valid_keys or [])
        if not valid_keys:
            return Action(key=None, rt_s=None, meta={"source": "movie_sampler", "reason": "no_valid_keys"})

        phase = str(obs.phase or "").strip().lower()
        if phase in {"instruction", "goodbye", "block"}:
            key = self.continue_key if self.continue_key in valid_keys else valid_keys[0]
            return Action(key=key, rt_s=self.rt_continue_s, meta={"source": "movie_sampler", "outcome": "continue"})

        return Action(key=None, rt_s=None, meta={"source": "movie_sampler", "outcome": "no_response"})
