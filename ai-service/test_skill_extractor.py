from app.services.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.section_parser import parse_sections
from app.services.skill_extractor import extract_skills


pdf_path = "uploads/resume.pdf"

text = extract_text_from_pdf(pdf_path) 
text = clean_text(text)

sections = parse_sections(text)

skills = extract_skills(sections)

print("\n========== EXTRACTED SKILLS ==========\n")

for skill in skills:
    print(skill)