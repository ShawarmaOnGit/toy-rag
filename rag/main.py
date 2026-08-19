from pathlib import Path
from openai import OpenAIError

from rag.operations.embedding import embed_ingestion
from rag.operations.extraction import extract_directory, clean_pages
from rag.operations.chunking import chunk_pages
from rag.pipeline import answer_question

def main():
    questions = [
        "What score do I need to pass this course?",
        "How many days do I have to request a regrade?",
        "Can I work with other students on take-home assignments?",
        "What is the policy for requesting an incomplete grade?",
        "How long is a standard semester?"
    ]

    pages = clean_pages(extract_directory(Path("rag/data/pdfs")))
    chunks = chunk_pages(pages)
    embedded_chunks = embed_ingestion(chunks)

    for question in questions:
        print(f"\n\n\nQuestion: {question}")

        try:
            answer = answer_question(question, embedded_chunks, chunks, 3)
        except OpenAIError as e:
            print(f"[API ERROR] question skipped: {e}")
            continue

        print(f"\nAnswer: {answer.answer}")
        print(f"\nSources:")
        for source in answer.sources:
            print(
                f"[Source {source.rank}: {source.chunk.filename}, Page {source.chunk.page}] "
                f"Score: {source.score:.3f}"
            )


if __name__ == "__main__":
    main()