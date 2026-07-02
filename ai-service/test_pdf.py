from app.services.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text

pdf_path = "uploads/ATS_RESUME_TCS.pdf"

text = extract_text_from_pdf(pdf_path)
text = clean_text(text)

print("\n========== EXTRACTED TEXT ==========\n")
print(text)