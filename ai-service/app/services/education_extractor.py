import re


def extract_education(sections):
    """
    Extract education details from the EDUCATION section.
    Works generically across varied resume formats.
    """

    education_text = sections.get("education", "")

    if not education_text:
        return []

    lines = [line.strip() for line in education_text.split("\n") if line.strip()]

    degree_keywords = [
        "b.tech", "btech", "b.e", "be ", "b.sc", "bsc", "bca", "bcom", "b.com",
        "b.a", "ba ", "m.tech", "mtech", "m.e", "me ", "m.sc", "msc",
        "mca", "mba", "phd", "ph.d", "doctor", "bachelor", "master",
        "diploma", "associate", "hsc", "ssc", "12th", "10th", "high school"
    ]

    year_pattern = re.compile(r"\b(19|20)\d{2}\b")
    gpa_pattern = re.compile(r"\b(cgpa|gpa|percentage|marks)\b", re.IGNORECASE)

    education = []
    current = {}

    def is_new_entry_start(line_lower):
        return any(keyword in line_lower for keyword in degree_keywords)

    def flush_current():
        if current and any(current.get(k) for k in ("degree", "institution", "year")):
            education.append(current.copy())

    for line in lines:
        lower = line.lower()

        # Start a new education entry when a degree keyword is found
        if is_new_entry_start(lower):
            # If current already has a degree, this is a new entry
            if current.get("degree"):
                flush_current()
                current = {}
            current["degree"] = line
            year_match = year_pattern.search(line)
            if year_match:
                current["year"] = year_match.group(0)
            continue

        year_match = year_pattern.search(line)
        if year_match and "year" not in current:
            current["year"] = year_match.group(0)
            # remaining text on the line (if any) could be institution
            remainder = year_pattern.sub("", line).strip(" ,-|")
            if remainder and "institution" not in current:
                current["institution"] = remainder
            continue

        if gpa_pattern.search(lower):
            current["gpa"] = line
            continue

        if "institution" not in current:
            current["institution"] = line
        elif "details" not in current:
            current["details"] = line
        else:
            current["details"] += " " + line

    flush_current()

    return education