from pprint import pprint

from app.services.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.section_parser import parse_sections
from app.services.certification_extractor import extract_certifications

text = extract_text_from_pdf("uploads/resume.pdf")

text = clean_text(text)

sections = parse_sections(text)

certifications = extract_certifications(sections)

print("\n========== CERTIFICATIONS ==========\n")

pprint(certifications)