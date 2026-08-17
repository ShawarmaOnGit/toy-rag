import numpy as np
from rag.models.chunk import Chunk
from rag.data.sample_chunks import SAMPLE_CHUNKS

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()
EMBEDDING_MODEL = "text-embedding-3-small"


def embed_ingestion(chunks: list[Chunk]) -> np.ndarray:
    if not chunks:
        raise ValueError("Chunks cannot be empty!")

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=[chunk.text for chunk in chunks]
    )

    embeddings = np.array([item.embedding for item in response.data])

    assert len(response.data) == len(chunks), \
        "There is a mismatch between chunks and embeddings"

    for i, item in enumerate(response.data):
        assert item.index == i, \
            "Chunks and embeddings order do not match"

    assert embeddings.shape == (len(chunks), 1536), \
        f"Embeddings is not in the right shape. Current shape: {embeddings.shape}"

    return embeddings


def embed_query(query: str) -> np.ndarray:
    if not query.strip():
        raise ValueError("Query cannot be empty!")

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=query
    )

    embedding = np.array(response.data[0].embedding)

    assert embedding.shape == (1536,), \
        f"Embedding is not in the right shape. Current shape: {embedding.shape}"

    return embedding


if __name__ == "__main__":
    embeddings = embed_ingestion(SAMPLE_CHUNKS)
    print(f"Embeddings shape: {embeddings.shape}")
    print(f"\nNumber of chunks: {len(SAMPLE_CHUNKS)}")
    print(f"\nFirst few values of first chunk: {embeddings[0][:5]}")