import numpy as np

from rag.models.chunk import Chunk
from rag.models.retrieval_result import RetrievalResult

def retrieve(query: np.ndarray, 
             embedded_chunks: np.ndarray, 
             chunks: list[Chunk], 
             top_k: int = 3) -> list[RetrievalResult]:
    pass