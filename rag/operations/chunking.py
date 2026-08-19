from rag.models.page import Page
from rag.models.chunk import Chunk


def chunk_pages(
    pages: list[Page],
    chunk_size: int = 100,
    overlap: int = 30,
    min_words: int = 20) -> list[Chunk]:
    """Split page records into overlapping chunk records, one page at a time."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than 0")

    if overlap < 0:
        raise ValueError("overlap cannot be negative")

    if overlap >= chunk_size:
        raise ValueError("overlap must be smaller than chunk_size")

    chunks = []
    for page in pages:
        words = page.text.split()
        chunk_index = 0

        for start in range(0, len(words), chunk_size - overlap):
            window = words[start:start + chunk_size]

            if len(window) < min_words:
                continue

            chunk_text = " ".join(window)

            chunk = Chunk(
                id=f"{page.filename}_p{page.page}_c{chunk_index}",
                text=chunk_text,
                filename=page.filename,
                page=page.page
            )

            chunks.append(chunk)
            chunk_index += 1

    return chunks