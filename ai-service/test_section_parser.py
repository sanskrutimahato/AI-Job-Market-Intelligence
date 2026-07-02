from app.services.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.section_parser import parse_sections

text = extract_text_from_pdf("uploads/resume.pdf")
text = clean_text(text)

sections = parse_sections(text)

print("\n========== RESUME SECTIONS ==========\n")

for section, content in sections.items():

    print("=" * 60)
    print(section.upper())
    print("=" * 60)
    print(content)
    print()