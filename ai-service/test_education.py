from app.services.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.section_parser import parse_sections
from app.services.education_extractor import extract_education

text = extract_text_from_pdf("uploads/resume.pdf")
text = clean_text(text)

sections = parse_sections(text)

education = extract_education(sections)

print("\n========== EDUCATION ==========\n")

print(education)