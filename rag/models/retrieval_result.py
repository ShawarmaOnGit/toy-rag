from pydantic import BaseModel

from rag.models.chunk import Chunk

class RetrievalResult(BaseModel):
    chunk: Chunk
    score: float
    rank: int