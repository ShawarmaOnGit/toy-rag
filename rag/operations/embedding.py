import numpy as np
from rag.models.chunk import Chunk

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def embed_ingestion(chunks: list[Chunk]) -> np.ndarray:
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=[chunk.text for chunk in chunks]
    )

    assert len(response.data) == len(chunks), "There is a mismatch between chunks and embeddings"

    for i, item in enumerate(response.data):
        assert item.index == i, "Chunks and embeddings order do not match"

    return np.array([item.embedding for item in response.data])


def embed_query(query: str) -> np.ndarray:
    pass
