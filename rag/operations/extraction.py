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


def extract_directory(pdf_dir: Path) -> list[Page]:
    """Run extract_pdf_pages over every PDF in a directory, flattened."""

    all_pages = []
    for path in sorted(pdf_dir.glob("*.pdf")):
        pages = extract_pdf_pages(path)
        all_pages.extend(pages)

    return all_pages
