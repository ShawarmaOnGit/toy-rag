from pydantic import BaseModel, ConfigDict
from typing import Literal

class EvalCase(BaseModel):
    model_config = ConfigDict(frozen=True)

    question: str
    kind: Literal["factual", "cross_context", "ambiguous", "unanswerable"]
    expected_sources: list[tuple[str, int]]
    note: str