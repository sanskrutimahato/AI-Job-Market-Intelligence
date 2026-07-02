import re
from difflib import SequenceMatcher

# Resume section headers and their common real-world variants.
SECTION_HEADERS = {
    "objective": [
        "objective", "career objective", "professional summary", "summary",
        "executive summary", "profile", "about me", "career profile",
        "career summary", "summary of qualifications", "personal summary",
    ],
    "experience": [
        "experience", "work experience", "professional experience",
        "employment history", "work history", "career history",
        "relevant experience", "internship", "internships",
        "internship experience", "professional background",
        "experience details", "positions held", "work details",
    ],
    "education": [
        "education", "academic background", "academic qualifications",
        "qualifications", "education & training", "education and training",
        "educational qualification", "educational background",
        "academic details", "scholastic record",
    ],
    "skills": [
        "skills", "technical skills", "technical expertise",
        "technical competencies", "core competencies", "core skills",
        "key skills", "competencies", "technologies", "relevant skills",
        "professional skills", "skill set", "technical proficiency",
        "areas of expertise", "tech stack", "technical stack",
        "programming languages", "tools & technologies",
        "tools and technologies", "soft skills", "skill highlights",
    ],
    "projects": [
        "projects", "academic projects", "personal projects",
        "major projects", "project experience", "key projects",
        "notable projects", "project work", "capstone project",
        "capstone projects",
    ],
# In SECTION_HEADERS, replace the "certifications" and "achievements" entries with:

    "certifications": [
        "certifications", "certificates", "professional certifications",
        "licenses", "training", "courses", "achievements & certifications",
        "certifications & courses", "online courses", "professional development",
        "certifications & awards", "awards & certifications",
        "certifications and awards", "awards and certifications",
        "certifications & achievements", "achievements & certifications",
        "courses & certifications", "certifications and courses",
        "licenses & certifications", "certifications, courses & achievements",
    ],
    "achievements": [
        "achievements", "awards", "honors", "honours", "accomplishments",
        "key achievements", "accomplishments & awards", "honors & awards",
        "awards & achievements", "achievements & awards",
        "scholarships", "scholarships & awards", "awards and honors",
    ],
    "contact": [
        "contact", "contact information", "personal information",
        "personal details", "address", "contact details",
    ],
    "languages": [
        "languages known", "languages", "spoken languages",
    ],
    "extracurricular": [
        "extracurricular activities", "extra curricular activities",
        "co curricular activities", "co-curricular activities",
        "activities",
    ],
    "publications": [
        "publications", "research papers", "papers published",
    ],
    "leadership": [
        "leadership", "leadership experience",
        "positions of responsibility", "responsibilities held",
    ],
    "volunteer": [
        "volunteer experience", "volunteering", "community service",
        "social work",
    ],
    "hobbies": [
        "hobbies", "interests", "hobbies and interests",
        "personal interests",
    ],
    "references": [
        "references", "references available upon request",
    ],
    "declaration": [
        "declaration",
    ],
}


def normalize_heading(text: str) -> str:
    """
    Normalize a heading-candidate string: lowercase, strip bullets,
    leading numbering (e.g. "1.", "II.", "a)"), and punctuation.
    """

    text = text.strip().lower()

    # Remove bullets
    text = re.sub(r"^[•\-\*\u2022\s]+", "", text)

    # Remove leading numbering / roman numerals / lettered enumeration
    text = re.sub(r"^\(?([0-9]+|[ivxlcdm]+|[a-z])[\.\)]\s*", "", text)

    # Remove punctuation
    text = re.sub(r"[:;|,_()\[\]{}\-/]+", " ", text)

    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


# Precomputed once at import time for fast exact-match lookup.
_NORMALIZED_HEADINGS = {
    normalize_heading(heading): section
    for section, headings in SECTION_HEADERS.items()
    for heading in headings
}


def _similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def is_heading(line: str, fuzzy_threshold: float = 0.84):
    """
    Return the section name if `line` looks like a section heading,
    otherwise None.

    Handles:
      - exact matches against known heading variants
      - minor typos / unseen variants via fuzzy matching
      - numbered or bulleted headings ("1. Skills", "- Education")
      - inline "Heading: content" lines ("Skills: Python, Java")
    """

    raw = line.strip()

    if not raw:
        return None

    # For lines like "Skills: Python, Java", only test the part before
    # the colon as the heading candidate.
    head_part = raw.split(":", 1)[0] if ":" in raw else raw

    normalized = normalize_heading(head_part)

    if not normalized or len(normalized.split()) > 5:
        return None

    # Pass 1: exact match against known headings.
    if normalized in _NORMALIZED_HEADINGS:
        return _NORMALIZED_HEADINGS[normalized]

    # Pass 2: fuzzy match to catch typos and unseen minor variants.
    # Restricted to short candidates to avoid misclassifying ordinary
    # sentences as headings.
    if len(normalized.split()) <= 4:
        best_section, best_score = None, 0.0

        for normalized_heading, section in _NORMALIZED_HEADINGS.items():
            score = _similarity(normalized, normalized_heading)

            if score > best_score:
                best_score, best_section = score, section

        if best_score >= fuzzy_threshold:
            return best_section

    return None


def parse_sections(text: str) -> dict:
    """
    Parse resume text into a dict of {section_name: content}.

    Generic across formats: numbered headings, bulleted headings,
    ALL CAPS headings, minor typos, and inline "Heading: content"
    lines are all handled without any resume-specific assumptions.
    """

    sections = {"other": ""}
    current_section = "other"

    lines = [
        line.rstrip()
        for line in text.splitlines()
        if line.strip()
    ]

    for line in lines:

        section = is_heading(line)

        if section:

            current_section = section

            if current_section not in sections:
                sections[current_section] = ""

            # Preserve inline content on the same line as the heading,
            # e.g. "Skills: Python, Java, SQL"
            if ":" in line:
                trailing = line.split(":", 1)[1].strip()

                if trailing:
                    sections[current_section] += trailing + "\n"

            continue

        sections[current_section] += line + "\n"

    cleaned = {}

    for section, content in sections.items():

        content = content.strip()

        if content:
            cleaned[section] = content

    return cleaned


if __name__ == "__main__":

    sample = """
    John Doe
    john.doe@email.com | +91 9876543210

    PROFESSIONAL SUMMARY
    Computer Science student interested in AI.

    1. Technical Skills
    Python
    Java
    SQL

    Skills: Docker, Git, AWS

    Work History
    Microsoft Intern
    Edunet Foundation Intern

    Eduction
    B.Tech CSE, RCOEM

    Key Projects
    AI Resume Parser
    Job Market Intelligence Platform

    Certifications & Courses
    Oracle Generative AI Professional

    Key Achievements
    Hackathon Winner

    Hobbies & Interests
    Sketching, Mandala Art
    """

    parsed = parse_sections(sample)

    for section, content in parsed.items():
        print("=" * 50)
        print(section.upper())
        print("=" * 50)
        print(content)
        print()