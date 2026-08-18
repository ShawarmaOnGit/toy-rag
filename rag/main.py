from rag.operations.retrieval import retrieve
from rag.operations.embedding import embed_ingestion, embed_query
from rag.data.sample_chunks import SAMPLE_CHUNKS

def main():
    questions = [
        "What score do I need to pass this course?",
        "How many days do I have to request a regrade?",
        "Can I work with other students on take-home assignments?",
        "What is the policy for requesting an incomplete grade?",
    ]

    embedded_chunks = embed_ingestion(SAMPLE_CHUNKS)

    for question in questions:
        print(f"Question: {question}")
        query = embed_query(question)
        results = retrieve(
            query=query,
            embedded_chunks=embedded_chunks,
            chunks=SAMPLE_CHUNKS,
            top_k=3
        )

        for result in results:
            print(f"Chunk: {result.chunk.text}")
            print(f"Score: {result.score}")
            print(f"Rank: {result.rank}\n")

if __name__ == "__main__":
    main()