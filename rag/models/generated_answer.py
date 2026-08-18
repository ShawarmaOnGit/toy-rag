from pydantic import BaseModel, ConfigDict

from rag.models.retrieval_result import RetrievalResult

class GeneratedAnswer(BaseModel):
    model_config = ConfigDict(frozen=True)

    answer: str
    sources: list[RetrievalResult]
    prompt: str
