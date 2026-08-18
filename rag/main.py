from rag.operations.retrieval import retrieve
from rag.operations.embedding import embed_ingestion, embed_query
from rag.operations.prompting import build_prompt
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
        query = embed_query(question)
        results = retrieve(
            query=query,
            embedded_chunks=embedded_chunks,
            chunks=SAMPLE_CHUNKS,
            top_k=3
        )

        prompt = build_prompt(question, results)
        print(prompt)
        print(f"\n----- Length of prompt: {len(prompt)} -----\n")
        assert all(r.chunk.text in prompt for r in results)
        assert all(r.chunk.filename in prompt for r in results)
        assert all(str(r.chunk.page) in prompt for r in results)
        assert question in prompt
        assert prompt.index(question) > prompt.index(results[0].chunk.text)   # question last

        labels = [f"Source {r.rank}" for r in results]
        assert len(set(labels)) == len(labels)                          # unique labels

        assert all(str(round(r.score, 2)) not in prompt for r in results)  # no score leak

        empty_prompt = build_prompt("Any question", [])
        assert "Any question" in empty_prompt


if __name__ == "__main__":
    main()