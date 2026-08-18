import numpy as np

from rag.models.chunk import Chunk
from rag.models.retrieval_result import RetrievalResult

def retrieve(query: np.ndarray, 
             embedded_chunks: np.ndarray, 
             chunks: list[Chunk], 
             top_k: int = 3) -> list[RetrievalResult]:

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0!")

    scores = embedded_chunks @ query / (np.linalg.norm(embedded_chunks, axis=1) * np.linalg.norm(query))  # (15,)
    top_indices = np.argsort(scores)[::-1][:top_k]

    results = []
    for rank, i in enumerate(top_indices, 1):
        result = RetrievalResult(
            chunk=chunks[i],
            score=float(scores[i]),
            rank=rank
        )
        results.append(result)

    return results