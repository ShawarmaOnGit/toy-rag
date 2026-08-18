import numpy as np

from rag.models.chunk import Chunk
from rag.models.retrieval_result import RetrievalResult
from rag.data.sample_chunks import SAMPLE_CHUNKS
from rag.operations.embedding import embed_query
from rag.operations.embedding import embed_ingestion

def retrieve(query: np.ndarray, 
             embedded_chunks: np.ndarray, 
             chunks: list[Chunk], 
             top_k: int = 3) -> list[RetrievalResult]:

    if top_k <= 0:
        raise ValueError("top_k must be greater than 0!")

    scores = embedded_chunks @ query / (np.linalg.norm(embedded_chunks, axis=1) * np.linalg.norm(query))
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


if __name__ == "__main__":
    query = embed_query("Can I work with others on assignments?")
    embedded_chunks = embed_ingestion(SAMPLE_CHUNKS)
    results = retrieve(query, embedded_chunks, SAMPLE_CHUNKS, 3)

    for result in results:
        print(f"\n{result}")