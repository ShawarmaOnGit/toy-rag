from pypdf import PdfReader
from pathlib import Path
from rag.models.page import Page

def extract_pdf_pages(path: Path) -> list[Page]:
    """Extract one PDF into raw, uncleaned per page records."""
    reader = PdfReader(path)
    pages = []

    for page_number, page in enumerate(reader.pages, 1):
        pages.append(
            Page(
                text=page.extract_text(),
                filename=path.name,
                page=page_number
            )
        )

    return pages


def extract_directory(pdf_dir: Path) -> list[Page]:
    """Run extract_pdf_pages over every PDF in a directory, flattened."""

    all_pages = []
    for path in sorted(pdf_dir.glob("*.pdf")):
        pages = extract_pdf_pages(path)
        all_pages.extend(pages)

    return all_pages


def clean_pages(pages: list[Page]) -> list[Page]:
    """Return a new list of Pages with normalised text."""

    cleaned_pages = []
    for page in pages:
        cleaned_text = " ".join(page.text.split())
        cleaned_page = page.model_copy(update={"text": cleaned_text})
        cleaned_pages.append(cleaned_page)

    return cleaned_pages