from pprint import pprint

from app.services.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.section_parser import parse_sections
from app.services.project_extractor import extract_projects

text = extract_text_from_pdf("uploads/sample_resume.pdf")

text = clean_text(text)

sections = parse_sections(text)

projects = extract_projects(sections)

print("\n========== PROJECTS ==========\n")

pprint(projects)

