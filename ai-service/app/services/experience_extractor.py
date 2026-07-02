import re


BULLET_CHARS = "•◦▪‣⁃●○*"

MONTHS = r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?"

DATE_TOKEN = rf"({MONTHS}\s*\d{{4}}|\d{{1,2}}/\d{{4}}|\d{{4}}|present|current|ongoing)"

DATE_PATTERN = re.compile(DATE_TOKEN, re.IGNORECASE)

DATE_RANGE_PATTERN = re.compile(
    rf"{DATE_TOKEN}\s*[-–—to]+\s*{DATE_TOKEN}|{DATE_TOKEN}",
    re.IGNORECASE,
)

# A line that IS (almost) entirely a date range, e.g. "Feb 2026 – Mar 2026"
DATE_LINE_PATTERN = re.compile(
    rf"^\s*{DATE_TOKEN}\s*([-–—]|to)\s*{DATE_TOKEN}\s*$|^\s*{DATE_TOKEN}\s*$",
    re.IGNORECASE,
)

ROLE_KEYWORDS = [
    "intern", "engineer", "developer", "analyst", "consultant",
    "manager", "designer", "scientist", "administrator", "specialist",
    "associate", "lead", "architect", "coordinator", "director",
    "officer", "researcher", "assistant", "executive", "head",
    "founder", "co-founder", "freelance", "volunteer", "trainee"
]

SECTION_STOP_WORDS = [
    "contact", "education", "skills", "projects", "certifications",
    "achievements", "summary", "objective", "references", "languages",
    "interests", "publications", "awards"
]

SEPARATOR_SPLIT = re.compile(r"\s*[–—|]\s*|\s+-\s+")


def clean_line(line: str) -> str:
    if not line:
        return ""
    line = line.replace("\uf0b7", "•")
    line = line.replace("\uf0a7", "•")
    line = line.replace("\x95", "•")
    line = line.strip()
    line = re.sub(r"\s+", " ", line)
    return line


def strip_bullet(line: str) -> str:
    return line.lstrip(BULLET_CHARS + " \t").strip()


def starts_with_bullet(line: str) -> bool:
    return bool(line) and line[0] in BULLET_CHARS


def has_date(line: str) -> bool:
    return bool(DATE_PATTERN.search(line))


def is_date_only_line(line: str) -> bool:
    return bool(DATE_LINE_PATTERN.match(line.strip()))


def is_role_line(line: str) -> bool:
    if not line or len(line) > 120 or starts_with_bullet(line):
        return False
    if is_date_only_line(line):
        return False

    lower = line.lower()
    if any(re.search(rf"\b{kw}\b", lower) for kw in ROLE_KEYWORDS):
        return True
    return False


def is_section_header(line: str) -> bool:
    lower = line.lower().strip(":").strip()
    return lower in SECTION_STOP_WORDS or any(
        lower.startswith(word) for word in SECTION_STOP_WORDS
    )


def split_role_company(line: str):
    """
    Split a role line like "Power BI Intern – Microsoft Elevate"
    into (role, company). If no separator/company part found,
    returns (line, "").
    """
    parts = SEPARATOR_SPLIT.split(line, maxsplit=1)
    if len(parts) == 2:
        role, company = parts[0].strip(), parts[1].strip()
        if role and company and not has_date(company):
            return role, company
    return line, ""


def parse_pipe_line(line: str):
    """Parse a line containing '|' into (company, location, duration)."""
    company, location, duration = "", "", ""
    segments = [s.strip() for s in line.split("|") if s.strip()]

    date_segs = [s for s in segments if has_date(s)]
    other_segs = [s for s in segments if s not in date_segs]

    if date_segs:
        duration = date_segs[0]

    if other_segs:
        first = other_segs[0]
        parts = [p.strip() for p in first.split(",") if p.strip()]
        if len(parts) >= 2:
            company = parts[0]
            location = ", ".join(parts[1:])
        else:
            company = parts[0] if parts else first
        if len(other_segs) > 1:
            location = location or other_segs[1]

    return company, location, duration


def is_header_candidate(line: str) -> bool:
    """
    A line that could plausibly be part of the role/company/location/date
    block (as opposed to a bullet/description sentence).
    """
    if not line or starts_with_bullet(line):
        return False
    if len(line.split()) > 8:
        return False
    if line.endswith((".", ":", ";")) and len(line.split()) > 4:
        return False
    return True


def extract_company_duration(line: str):
    """Generic single-line company/location/duration extractor."""
    if "|" in line:
        return parse_pipe_line(line)

    company, location, duration = "", "", ""
    match = DATE_RANGE_PATTERN.search(line)

    if match:
        duration = match.group(0).strip()
        left = (line[: match.start()] + line[match.end():]).strip(" ,-–—")
    else:
        left = line.strip()

    parts = [p.strip() for p in left.split(",") if p.strip()]
    if len(parts) >= 2:
        company = parts[0]
        location = ", ".join(parts[1:])
    elif parts:
        company = parts[0]

    return company, location, duration


def extract_experience(sections):
    text = (
        sections.get("experience", "")
        or sections.get("work experience", "")
        or sections.get("professional experience", "")
    )

    if not text:
        return []

    lines = [clean_line(line) for line in text.split("\n")]
    lines = [line for line in lines if line]

    experiences = []
    current = None

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]

        if is_section_header(line):
            break

        if is_role_line(line):
            if current:
                experiences.append(current)

            role, inline_company = split_role_company(line)

            current = {
                "role": role,
                "company": inline_company,
                "location": "",
                "duration": "",
                "description": [],
            }

            # Consume subsequent header lines (company/location/duration)
            # until a bullet or a clearly descriptive line is reached.
            j = i + 1
            consumed = 0
            while j < n and consumed < 4 and is_header_candidate(lines[j]):
                nxt = lines[j]

                if is_section_header(nxt) or is_role_line(nxt):
                    break

                if "|" in nxt:
                    company, location, duration = parse_pipe_line(nxt)
                    current["company"] = current["company"] or company
                    current["location"] = current["location"] or location
                    current["duration"] = current["duration"] or duration
                elif is_date_only_line(nxt):
                    current["duration"] = current["duration"] or nxt
                elif has_date(nxt):
                    company, location, duration = extract_company_duration(nxt)
                    current["company"] = current["company"] or company
                    current["location"] = current["location"] or location
                    current["duration"] = current["duration"] or duration
                else:
                    # Plain short line: treat as company if missing, else location
                    if not current["company"]:
                        current["company"] = nxt
                    elif not current["location"]:
                        current["location"] = nxt
                    else:
                        break

                j += 1
                consumed += 1

            i = j
            continue

        # Bullet / description line
        if current:
            bullet = strip_bullet(line)
            if bullet:
                current["description"].append(bullet)

        i += 1

    if current:
        experiences.append(current)

    return experiences