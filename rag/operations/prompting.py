from rag.models.retrieval_result import RetrievalResult

def build_prompt(question: str, results: list[RetrievalResult]) -> str:
    INSTRUCTIONS = (
        "Answer using only the context below. If the context does not have enough "
        "information to answer the question, say so explicitly rather than guessing, "
        "using pretrained knowledge, or picking a side anyways.\n"
        "Also, if the context contradicts each other, say so explcitly instead of "
        "guessing or picking a side.\n"
        "Cite the sources for each claim."
    )
