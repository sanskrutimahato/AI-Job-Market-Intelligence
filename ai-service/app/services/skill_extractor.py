"""
skill_extractor.py
-------------------
Unified, reusable skill extraction module for the AI-Powered Job Market
Intelligence Platform.

This single module is used in TWO places:

    1. Resume Parsing Pipeline
       resume_parser.py calls extract_skills() with the isolated
       "Skills" section text produced by section_parser.py.

    2. Job Match Engine
       job_match_engine.py calls extract_skills() with the FULL raw
       job description text (which has no dedicated "Skills" section).

Design:
    - If the input text "looks like" a dedicated skills section
      (short, delimiter-separated, no prose/sentence structure),
      we use the ORIGINAL legacy behaviour: split on common
      delimiters and take each cleaned token as a skill, as-is.
      This preserves the ability to capture arbitrary/custom skills
      that aren't in our predefined master list (e.g. "Photoshop",
      "Public Speaking") -- exactly how the resume parser behaves today.

    - If the input text does NOT look like a dedicated skills section
      (i.e. it's prose, like a job description), we fall back to
      scanning the FULL text against a curated, extensible master
      list of technical skills using case-insensitive, boundary-safe
      regex matching.

Both paths:
    - are case-insensitive when matching
    - remove duplicates
    - preserve the order in which skills first appear in the text
"""

import re
from typing import Any, Dict, List, Set, Union


# ---------------------------------------------------------------------------
# 1. MASTER SKILL LIST
# ---------------------------------------------------------------------------
# Single source of truth for technical skills used in the full-text
# (job description) fallback path. Extend this list to recognize more
# skills -- no other code changes are required.
#
# NOTE: Order here does not affect output order (output order is based on
# position of first appearance in the text), so feel free to append new
# skills anywhere in this list.
MASTER_SKILLS: List[str] = [
    # Languages
    "Python", "Java", "C++", "C#", "JavaScript", "TypeScript",
    # Frontend
    "React", "Angular", "Vue", "HTML", "CSS", "Bootstrap", "Tailwind CSS",
    # Backend / Frameworks
    "Node.js", "Express", "FastAPI", "Flask", "Django", "Spring Boot",
    # Databases
    "MongoDB", "MySQL", "PostgreSQL", "SQL", "Redis",
    # DevOps / Cloud
    "Docker", "Kubernetes", "Git", "GitHub", "AWS", "Azure", "GCP",
    "Jenkins", "CI/CD", "Linux",
    # APIs
    "REST API", "GraphQL",
    # Data / ML
    "TensorFlow", "PyTorch", "Pandas", "NumPy", "Scikit-learn",
]

# Sort by length (longest first) so that multi-word / longer skills like
# "Spring Boot" or "REST API" are checked before shorter potential
# substrings, keeping matching predictable and greedy.
_SORTED_MASTER_SKILLS = sorted(MASTER_SKILLS, key=len, reverse=True)


# ---------------------------------------------------------------------------
# 2. STOPWORDS TO IGNORE
# ---------------------------------------------------------------------------
# Common English / job-description filler words that should NEVER be
# treated as skills, even if they slip into a delimiter-split token
# (e.g. a messy resume "Skills" line, or a stray fragment).
STOPWORDS_TO_IGNORE: Set[str] = {
    "looking", "for", "with", "experience", "developer", "engineer",
    "candidate", "responsibilities", "responsible", "requirements",
    "required", "preferred", "skills", "and", "or", "the", "a", "an",
    "in", "of", "to", "is", "are", "we", "our", "you", "your", "will",
    "must", "have", "has", "years", "year", "team", "join", "role",
    "strong", "good", "excellent", "knowledge", "understanding",
    "ability", "proficient", "proficiency", "familiarity", "familiar",
    "plus", "etc", "including", "such", "as", "who", "can", "should",
}

# Phrases that strongly indicate the text is PROSE (a job description /
# paragraph) rather than a clean, dedicated "Skills:" list.
_PROSE_MARKERS = [
    "looking for", "responsible for", "years of experience", "we are",
    "requirements", "responsibilities", "join our team", "must have",
    "should have", "nice to have", "about the role", "about us",
    "who you are", "what you'll do", "what you will do",
]


# ---------------------------------------------------------------------------
# 3. PUBLIC ENTRY POINT
# ---------------------------------------------------------------------------
def extract_skills(source: Union[str, Dict[str, Any]]) -> List[str]:
    """
    Extract skills from EITHER a resume's parsed `sections` dict OR a
    raw job description string, using the same public API.

    Args:
        source: Either
              - the `sections` dict produced by section_parser.py
                (as used by resume_parser.py, matching the calling
                convention of extract_education(sections),
                extract_experience(sections), etc.), or
              - the isolated "Skills" section text on its own, or
              - the full raw job description text (no dedicated
                skills section) as used by job_match_engine.py.

    Returns:
        A list of skills, deduplicated, in the order they first
        appear in the resolved text. Returns [] for empty/None input.
    """
    text = _resolve_input_text(source)

    if not text or not text.strip():
        return []

    if _looks_like_dedicated_skills_section(text):
        # Resume-style input: preserve existing behaviour exactly.
        skills = _extract_from_skills_section(text)
        if skills:
            return skills
        # Fall through to full-text scan as a safety net in case the
        # "skills section" heuristic misfired and the split logic
        # yielded nothing usable.

    # Job-description-style input (or fallback): scan the full text
    # against the curated master skill list.
    return _extract_from_full_text(text)


# ---------------------------------------------------------------------------
# 3b. INPUT RESOLUTION: dict (sections) vs plain string
# ---------------------------------------------------------------------------
# Common keys section_parser.py might use for the skills section.
# Add more variants here if your section_parser uses different headers.
_SKILLS_SECTION_KEYS = ("skills", "skill", "technical_skills", "technical skills")


def _resolve_input_text(source: Union[str, Dict[str, Any]]) -> str:
    """
    Normalize the incoming argument into a plain string to run
    extraction on.

    - If `source` is already a string (e.g. a raw job description
      passed by job_match_engine.py), it's used as-is.
    - If `source` is a dict (e.g. the `sections` dict passed by
      resume_parser.py, matching the pattern used by the other
      extractors), pull out the skills-related section. If no
      dedicated skills section exists, fall back to concatenating
      all section text so skills mentioned inline can still be
      picked up by the full-text scan.
    """
    if isinstance(source, str):
        return source

    if isinstance(source, dict):
        for key in _SKILLS_SECTION_KEYS:
            value = source.get(key)
            if value:
                return value if isinstance(value, str) else " ".join(str(v) for v in value)

        # No dedicated skills section found -- fall back to every
        # section's text combined, so the full-text scan still has
        # a chance to find skills mentioned elsewhere (e.g. in an
        # "Experience" or "Summary" section).
        return " ".join(str(v) for v in source.values() if v)

    return ""


# ---------------------------------------------------------------------------
# 4. HEURISTIC: is this a dedicated "Skills" section or prose?
# ---------------------------------------------------------------------------
def _looks_like_dedicated_skills_section(text: str) -> bool:
    """
    Decide whether `text` looks like a short, delimiter-separated
    skills list (typical resume "Skills" section) as opposed to
    free-flowing prose (typical job description paragraph).
    """
    stripped = text.strip()
    if not stripped:
        return False

    lower = stripped.lower()

    # Strong signal: prose phrases that only appear in job description
    # style writing, never in a clean skills list.
    if any(marker in lower for marker in _PROSE_MARKERS):
        return False

    # Split on common resume "skills" delimiters.
    tokens = [t.strip() for t in re.split(r"[,\n•|;/]+", stripped) if t.strip()]

    if len(tokens) < 2:
        # Single token / very short text -- treat as skills-section-like
        # only if it's short (e.g. "Python" or "Python, FastAPI" split
        # into one token because no delimiter was used).
        return len(stripped.split()) <= 6

    # Dedicated skills lists tend to have short tokens
    # (e.g. "Python", "Machine Learning") rather than full sentences.
    avg_words_per_token = sum(len(t.split()) for t in tokens) / len(tokens)
    return avg_words_per_token <= 3


# ---------------------------------------------------------------------------
# 5. LEGACY PATH: split-based extraction (resume "Skills" section)
# ---------------------------------------------------------------------------
def _extract_from_skills_section(text: str) -> List[str]:
    """
    Original resume extraction logic: split the isolated Skills
    section on common delimiters and treat each cleaned token as a
    skill, preserving whatever the resume author wrote (so custom /
    niche skills not in MASTER_SKILLS are still captured).
    """
    raw_tokens = re.split(r"[,\n•|;/]+", text)

    skills: List[str] = []
    seen: Set[str] = set()

    for token in raw_tokens:
        # Strip whitespace and common bullet/dash characters.
        cleaned = re.sub(r"^[\s\-*•]+|[\s\-*•]+$", "", token).strip()
        if not cleaned:
            continue

        lower = cleaned.lower()

        # Skip filler/stopwords that shouldn't be treated as a skill.
        if lower in STOPWORDS_TO_IGNORE:
            continue

        # Case-insensitive duplicate removal, order-preserving.
        if lower in seen:
            continue

        seen.add(lower)
        skills.append(cleaned)

    return skills


# ---------------------------------------------------------------------------
# 6. FALLBACK PATH: full-text scan against MASTER_SKILLS (job descriptions)
# ---------------------------------------------------------------------------
def _extract_from_full_text(text: str) -> List[str]:
    """
    Scan free-flowing text (e.g. a job description) for known
    technical skills from MASTER_SKILLS.

    Uses case-insensitive, boundary-safe regex matching so that:
        - "Node.js" doesn't get chopped into "Node"
        - "C++" and "C#" are matched literally (not as regex noise)
        - "SQL" does NOT falsely match inside "MySQL" or "PostgreSQL"
          (boundary check ensures the char immediately before/after
          the match is not alphanumeric)

    Returns skills in the canonical casing from MASTER_SKILLS, ordered
    by first appearance in the text.
    """
    matches: List[tuple] = []  # (start_index, canonical_skill_name)
    seen: Set[str] = set()

    for skill in _SORTED_MASTER_SKILLS:
        lower_skill = skill.lower()
        if lower_skill in seen:
            continue

        # Custom boundary check instead of \b, because \b does not
        # behave well around special characters like '+', '#', '.', '/'
        # which appear in skills such as "C++", "C#", "Node.js", "CI/CD".
        pattern = re.compile(
            r"(?<![A-Za-z0-9])" + re.escape(skill) + r"(?![A-Za-z0-9])",
            re.IGNORECASE,
        )
        match = pattern.search(text)
        if match:
            matches.append((match.start(), skill))
            seen.add(lower_skill)

    # Preserve order of first appearance in the original text.
    matches.sort(key=lambda m: m[0])
    return [skill for _, skill in matches]


# ---------------------------------------------------------------------------
# 7. Dual invocation support (direct script run + package import)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Quick manual sanity check when running this file directly:
    #   python skill_extractor.py

    resume_skills_section = """
    Python, FastAPI, Docker, Git, MongoDB, Machine Learning, Photoshop
    """

    job_description = (
        "We are looking for a Python Developer with experience in "
        "Python, FastAPI, Docker, MongoDB, AWS and Git. The candidate "
        "should also have knowledge of REST API design and CI/CD pipelines."
    )

    # Simulates the `sections` dict produced by section_parser.py, which
    # is what resume_parser.py actually passes in.
    sections_dict = {
        "education": "B.Tech Computer Science, RCOEM, Nagpur",
        "skills": "Python, FastAPI, Docker, Git, MongoDB, Machine Learning, Photoshop",
        "experience": "Worked as a backend intern building REST APIs.",
    }

    print("Resume Skills Section (string) ->", extract_skills(resume_skills_section))
    print("Resume sections dict           ->", extract_skills(sections_dict))
    print("Job Description (string)       ->", extract_skills(job_description))