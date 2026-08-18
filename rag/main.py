from openai import OpenAIError

from rag.operations.embedding import embed_ingestion
from rag.data.sample_chunks import SAMPLE_CHUNKS
from rag.pipeline import answer_question

def main():
    questions = [
        "What score do I need to pass this course?",
        "How many days do I have to request a regrade?",
        "Can I work with other students on take-home assignments?",
        "What is the policy for requesting an incomplete grade?",
        "How long is a standard semester?"
    ]

    embedded_chunks = embed_ingestion(SAMPLE_CHUNKS)

    for question in questions:
        print(f"\n\n\nQuestion: {question}")

        try:
            answer = answer_question(question, embedded_chunks, SAMPLE_CHUNKS, 3)
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