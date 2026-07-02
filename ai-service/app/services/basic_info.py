import re
import spacy

# Load SpaCy model only once
nlp = spacy.load("en_core_web_sm")


def extract_name(text: str):
    """
    Extract candidate name.
    First tries SpaCy PERSON entity.
    If unavailable, returns the first meaningful line.
    """

    doc = nlp(text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text.strip()

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if (
            len(line.split()) >= 2
            and len(line) < 40
            and "resume" not in line.lower()
            and "curriculum" not in line.lower()
        ):
            return line

    return ""


def extract_email(text: str):

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    return match.group() if match else ""


def extract_phone(text: str):

    pattern = r"(\+?\d{1,3}[-.\s]?)?(\(?\d{3}\)?[-.\s]?)?\d{3}[-.\s]?\d{4}"

    match = re.search(pattern, text)

    return match.group() if match else ""


def extract_linkedin(text: str):

    pattern = r"(https?:\/\/)?(www\.)?linkedin\.com\/in\/[A-Za-z0-9_-]+"

    match = re.search(pattern, text)

    return match.group() if match else ""


def extract_github(text: str):

    pattern = r"(https?:\/\/)?(www\.)?github\.com\/[A-Za-z0-9_-]+"

    match = re.search(pattern, text)

    return match.group() if match else ""


def extract_basic_info(text: str):

    return {

        "name": extract_name(text),

        "email": extract_email(text),

        "phone": extract_phone(text),

        "linkedin": extract_linkedin(text),

        "github": extract_github(text)

    }