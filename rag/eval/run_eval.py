import numpy as np

from rag.models.chunk import Chunk
from rag.models.questions import EvalCase, TEST_QUESTIONS
from rag.models.retrieval_evaluation import RetrievalEvaluation
from rag.operations.embedding import embed_query
from rag.operations.retrieval import retrieve


def evaluate_retrieval(
    cases: list[EvalCase],
    embeddings: np.ndarray,
    chunks: list[Chunk],
    top_k: int = 3) -> list[RetrievalEvaluation]:
    # precondition: alignment must hold before any of this means anything
    assert len(chunks) == embeddings.shape[0], "chunk/embedding misalignment"
    assert len({c.id for c in chunks}) == len(chunks), "duplicate chunk ids"

    outcomes = []
    for case in cases:
        question_vector = embed_query(case.question)
        results = retrieve(question_vector, embeddings, chunks, top_k)

        retrieved_set = {(r.chunk.filename, r.chunk.page) for r in results}
        ranks_by_result = {
            (r.chunk.filename, r.chunk.page): r.rank for r in results
        }

        if case.kind == "unanswerable":
            hit = None
            ranks = {}
        else:
            ranks = {
                src: ranks_by_result.get(src)  # None if not retrieved
                for src in case.expected_sources
            }
            hit = all(rank is not None for rank in ranks.values())

        outcomes.append(
            RetrievalEvaluation(
                case=case,
                hit=hit,
                ranks=ranks,
                retrieved=results,
            )
        )

    return outcomes


if __name__ == "__main__":
    from pathlib import Path
    from rag.operations.extraction import extract_directory, clean_pages
    from rag.operations.chunking import chunk_pages
    from rag.operations.embedding import embed_ingestion

    pages = clean_pages(extract_directory(Path("rag/data/pdfs")))
    chunks = chunk_pages(pages)
    embeddings = embed_ingestion(chunks)

    outcomes = evaluate_retrieval(TEST_QUESTIONS, embeddings, chunks, top_k=3)

    answerable = [o for o in outcomes if o.hit is not None]
    hits = sum(1 for o in answerable if o.hit)

    for i, o in enumerate(outcomes, 1):
        status = "N/A" if o.hit is None else ("HIT" if o.hit else "MISS")
        rank_str = ", ".join(
            f"{src[0]}p{src[1]}:{r}" for src, r in o.ranks.items()
        ) or "-"
        print(f"{i:<3} {o.case.kind:<14} {status:<5} {rank_str:<30} {o.case.question[:50]}")

    print(f"\nhit {hits}/{len(answerable)} answerable questions")