import re

BULLET_CHARS = r"•●▪■‣◦·–—\-\*"


def clean_skill(skill: str) -> str:
    skill = skill.strip()
    skill = re.sub(rf"^[{BULLET_CHARS}]+\s*", "", skill)
    skill = re.sub(r"^\(?([0-9]+|[a-zA-Z])[\.\)]\s*", "", skill)
    skill = re.sub(r"\s+", " ", skill)
    skill = re.sub(r"[.;:,]\s*$", "", skill)
    return skill.strip()


def _split_line(line: str):
    """
    Split one raw line into individual skill tokens.
    Handles commas, semicolons, pipes, bullets, and
    multi-space column-formatted rows.
    """
    # Drop category label before colon e.g. "Languages: Python, Java"
    if ":" in line:
        line = line.split(":", 1)[1]

    # Normalize "and" into comma when already comma-separated
    if "," in line:
        line = re.sub(r"\s+and\s+", ", ", line)

    if re.search(r"[,;|•●▪■]", line):
        parts = re.split(r"[,;|•●▪■]", line)
    elif re.search(r"\s{2,}", line):
        parts = re.split(r"\s{2,}", line)
    else:
        parts = [line]

    return parts


def _get_skills_text(input_data) -> str:
    """
    Accept either:
      - a dict  (sections map)  → pull 'skills' key
      - a str   (raw resume text) → extract the skills block manually
    """
    if isinstance(input_data, dict):
        return (
            input_data.get("skills", "")
            or input_data.get("technical skills", "")
            or input_data.get("core skills", "")
            or input_data.get("key skills", "")
            or ""
        )

    if isinstance(input_data, str):
        # Find the skills section inside raw text using a simple header scan
        lines = input_data.splitlines()
        skill_headers = {
            "skills", "technical skills", "core skills", "key skills",
            "competencies", "technologies", "tech stack", "skill set",
            "technical expertise", "technical proficiency",
            "areas of expertise", "tools & technologies",
            "tools and technologies", "programming languages",
        }
        next_section_pattern = re.compile(
            r"^(experience|education|projects|certifications|achievements|"
            r"objective|summary|contact|references|languages|hobbies|"
            r"publications|leadership|volunteer|declaration|awards)\b",
            re.IGNORECASE,
        )

        in_section = False
        collected = []

        for line in lines:
            normalized = re.sub(r"[^a-z\s]", "", line.strip().lower()).strip()

            if not in_section:
                if normalized in skill_headers:
                    in_section = True
                continue

            # Stop at the next section header
            if next_section_pattern.match(line.strip()):
                break

            collected.append(line)

        return "\n".join(collected)

    return ""


def extract_skills(input_data) -> list:
    """
    Extract skills from either:
      - a sections dict  (output of section_parser)
      - a raw text string (full resume text)

    Returns a deduplicated ordered list of skill strings.
    """
    skills_text = _get_skills_text(input_data)

    if not skills_text or not skills_text.strip():
        return []

    extracted = []

    for line in skills_text.split("\n"):
        line = line.strip()
        if not line:
            continue

        for part in _split_line(line):
            skill = clean_skill(part)

            if not skill:
                continue

            # Must contain at least one letter
            if not re.search(r"[A-Za-z]", skill):
                continue

            # Drop sentence-like fragments
            if len(skill.split()) > 6:
                continue

            # Drop multi-word ALL-CAPS section header leakage
            words = skill.split()
            if len(words) > 1 and skill == skill.upper():
                continue

            extracted.append(skill)

    # Deduplicate preserving order, case-insensitive
    seen = set()
    unique = []
    for skill in extracted:
        key = skill.lower()
        if key not in seen:
            seen.add(key)
            unique.append(skill)

    return unique


if __name__ == "__main__":
    from pprint import pprint

    # Test with sections dict
    sections_input = {
        "skills": (
            "Languages: Python, Java, C++\n"
            "Frameworks: React, Node.js, Flask\n"
            "Tools: Git, Docker, AWS\n"
            "Databases: MongoDB, MySQL\n"
            "Soft Skills: Communication, Leadership and Teamwork"
        )
    }
    print("--- sections dict ---")
    pprint(extract_skills(sections_input))

    # Test with raw text string
    raw_text = """
    John Doe | john@example.com

    TECHNICAL SKILLS
    Languages: Python, Java, C++
    Frameworks: React, Node.js, Flask
    Tools: Git, Docker, AWS

    EXPERIENCE
    Software Engineer at XYZ
    """
    print("\n--- raw text string ---")
    pprint(extract_skills(raw_text))