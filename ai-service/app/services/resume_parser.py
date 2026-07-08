import traceback

from app.services.pdf_parser import extract_text_from_pdf
from app.utils.text_cleaner import clean_text

from app.services.basic_info import extract_basic_info
from app.services.section_parser import parse_sections
from app.services.skill_extractor import extract_skills
from app.services.education_extractor import extract_education
from app.services.experience_extractor import extract_experience
from app.services.project_extractor import extract_projects
from app.services.certification_extractor import extract_certifications


def safe_extract(fn, *args, fallback=None, label=""):
    """
    Run an extractor function safely. If it raises an exception, log the
    error and return a fallback value instead of crashing the whole
    pipeline.
    """
    try:
        return fn(*args)
    except Exception as e:
        print(f"[parse_resume] WARNING: {label} failed — {e}")
        traceback.print_exc()
        return fallback if fallback is not None else ([] if label != "basic_info" else {})


def parse_resume(pdf_path: str) -> dict:
    """
    Complete Resume Parser Pipeline.

    Input:  path to a PDF resume
    Output: dict with all extracted resume fields
    """

    # ── 1. Extract raw text ───────────────────────────────────────────────
    text = safe_extract(extract_text_from_pdf, pdf_path, fallback="", label="pdf_parser")
    if not text or not text.strip():
        return {
            "error": "Could not extract text from PDF. File may be scanned/image-based.",
            "name": "", "email": "", "phone": "",
            "linkedin": "", "github": "", "portfolio": "",
            "skills": [], "education": [], "experience": [],
            "projects": [], "certifications": [], "raw_text": "",
        }

    # ── 2. Clean text ─────────────────────────────────────────────────────
    text = safe_extract(clean_text, text, fallback=text, label="text_cleaner")

    # ── 3. Basic info ─────────────────────────────────────────────────────
    basic_info = safe_extract(extract_basic_info, text, fallback={}, label="basic_info")

    # ── 4. Section parsing ────────────────────────────────────────────────
    sections = safe_extract(parse_sections, text, fallback={}, label="section_parser")
    if not sections:
        sections = {}

    # ── 5. Individual extractors ────────────────────────────────────────────
    skills = safe_extract(extract_skills, sections, fallback=[], label="skills")
    education = safe_extract(extract_education, sections, fallback=[], label="education")
    experience = safe_extract(extract_experience, sections, fallback=[], label="experience")
    projects = safe_extract(extract_projects, sections, fallback=[], label="projects")
    certifications = safe_extract(extract_certifications, sections, fallback=[], label="certifications")

    # ── 6. Assemble output ───────────────────────────────────────────────
    return {
        "name": basic_info.get("name", ""),
        "email": basic_info.get("email", ""),
        "phone": basic_info.get("phone", ""),
        "linkedin": basic_info.get("linkedin", ""),
        "github": basic_info.get("github", ""),
        "portfolio": basic_info.get("portfolio", ""),
        "skills": skills if isinstance(skills, list) else [],
        "education": education if isinstance(education, list) else [],
        "experience": experience if isinstance(experience, list) else [],
        "projects": projects if isinstance(projects, list) else [],
        "certifications": certifications if isinstance(certifications, list) else [],
        "raw_text": text,
    }