from pypdf import PdfReader
from pathlib import Path

course_syllabus = Path("rag/data/pdfs/course_syllabus.pdf")
reader = PdfReader(course_syllabus)

text = reader.pages[0].extract_text()

print(text)