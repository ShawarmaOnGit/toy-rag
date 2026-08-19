from pydantic import BaseModel, ConfigDict

from rag.models.questions import EvalCase
from rag.models.retrieval_result import RetrievalResult


class RetrievalEvaluation(BaseModel):
    model_config = ConfigDict(frozen=True)

    case: EvalCase
    hit: bool | None
    ranks: dict[tuple[str, int], int | None]
    retrieved: list[RetrievalResult]