from pprint import pprint

from app.services.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.section_parser import parse_sections
from app.services.experience_extractor import extract_experience

text = extract_text_from_pdf("uploads/sample_resume.pdf")
text = clean_text(text)

sections = parse_sections(text)

experience = extract_experience(sections)

print("\n========== EXPERIENCE ==========\n")

pprint(experience, width=120)