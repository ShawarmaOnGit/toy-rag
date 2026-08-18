import numpy as np

from rag.models.chunk import Chunk
from rag.operations.embedding import embed_query
from rag.models.generated_answer import GeneratedAnswer
from rag.operations.retrieval import retrieve
from rag.operations.prompting import build_prompt
from rag.operations.generation import generate_answer

def answer_question(question: str, 
                    embedded_chunks: np.ndarray,
                    chunks: list[Chunk],
                    top_k: int = 3) -> GeneratedAnswer:

    if not question.strip():
        raise ValueError("Question cannot be empty!")

    embedded_question = embed_query(question)
    results = retrieve(embedded_question, embedded_chunks, chunks, top_k)
    prompt = build_prompt(question, results)
    answer = generate_answer(prompt)

    return GeneratedAnswer(
        answer=answer,
        sources=results,
        prompt=prompt
    )