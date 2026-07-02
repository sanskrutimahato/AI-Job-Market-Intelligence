from app.services.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text
from app.services.basic_info import extract_basic_info


pdf_path = "uploads/resume.pdf"

text = extract_text_from_pdf(pdf_path)

text = clean_text(text)

info = extract_basic_info(text)

print("\n========== BASIC INFO ==========\n")

for key, value in info.items():
    print(f"{key}: {value}")