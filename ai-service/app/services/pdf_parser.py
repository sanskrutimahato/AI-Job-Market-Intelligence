import fitz


def extract_text_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file using PyMuPDF.
    """

    text = ""

    try:
        document = fitz.open(pdf_path)

        for page in document:
            text += page.get_text()

        document.close()

    except Exception as e:
        raise Exception(f"Error reading PDF: {e}")

    return text