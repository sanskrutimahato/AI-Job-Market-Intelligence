import re


BULLET_CHARS = "•◦▪‣⁃●○*"
DASH_BULLET = re.compile(r"^[–—\-]\s+")
NUMBERED_PATTERN = re.compile(r"^\s*\d+[\.\)]\s+")

MONTHS = r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?"
DATE_TOKEN = rf"({MONTHS}\s*\d{{4}}|\d{{1,2}}/\d{{4}}|\d{{4}}|present|current|ongoing)"
DATE_RANGE_PATTERN = re.compile(
    rf"{DATE_TOKEN}\s*[-–—to]+\s*{DATE_TOKEN}|{DATE_TOKEN}", re.IGNORECASE
)
DATE_LINE_PATTERN = re.compile(
    rf"^\s*{DATE_TOKEN}\s*([-–—]|to)\s*{DATE_TOKEN}\s*$|^\s*{DATE_TOKEN}\s*$",
    re.IGNORECASE,
)

SECTION_STOP_WORDS = [
    "contact", "education", "skills", "experience", "work experience",
    "professional experience", "certifications", "achievements", "summary",
    "objective", "references", "languages", "interests", "publications",
    "awards", "certifications & awards"
]

TECH_LABEL_PATTERN = re.compile(
    r"^\s*(tech\s*stack|technologies|tools?\s*used|stack|built\s*with|tools?)\s*[:\-]",
    re.IGNORECASE,
)

LINK_PATTERN = re.compile(
    r"(https?://\S+|github\.com/\S+|\S+\.(?:com|io|dev|app)\S*)", re.IGNORECASE
)

TITLE_SEP = re.compile(r"\s*[–—|]\s*")

# Matches "ProjectName - rest of description" inside a bullet
# Title part: 1-5 words, title-cased, no lowercase start
INLINE_TITLE_PATTERN = re.compile(
    r"^([A-Z][A-Za-z0-9&\s\-\.]{1,50}?)\s+[-–—]\s+(.+)$"
)


def clean_line(line: str) -> str:
    if not line:
        return ""
    line = line.replace("\uf0b7", "•").replace("\uf0a7", "•").replace("\x95", "•")
    return re.sub(r"\s+", " ", line.strip())


def is_bullet(line: str) -> bool:
    if not line:
        return False
    if line[0] in BULLET_CHARS:
        return True
    if NUMBERED_PATTERN.match(line):
        return True
    if DASH_BULLET.match(line) and len(line.split()) >= 3:
        return True
    return False


def strip_bullet_marker(line: str) -> str:
    line = NUMBERED_PATTERN.sub("", line)
    line = DASH_BULLET.sub("", line)
    return line.lstrip(BULLET_CHARS + " \t").strip()


def is_section_header(line: str) -> bool:
    lower = line.lower().strip(": ").strip()
    return lower in SECTION_STOP_WORDS or any(
        lower.startswith(w) for w in SECTION_STOP_WORDS
    )


def ends_with_open(text: str) -> bool:
    t = text.rstrip()
    if not t:
        return False
    if t.endswith(","):
        return True
    last = t.split()[-1].lower().strip(",")
    return last in {
        "and", "or", "&", "for", "with", "the", "a", "an",
        "using", "by", "to", "of", "in", "via", "from", "on",
        "achieving", "including", "such", "as"
    }


def ends_sentence(text: str) -> bool:
    return text.strip().endswith((".", "!", "?", ";"))


def starts_like_continuation(line: str) -> bool:
    if not line:
        return False
    if line[0].islower() or line[0].isdigit():
        return True
    first_word = line.split()[0].lower().strip(",.;:")
    return first_word in {"and", "or", "&", "with", "using", "to", "of", "from"}


def is_inline_titled_bullet(text: str) -> bool:
    """
    Detect bullets of the form 'ProjectName - description...'
    where the title part is short (≤6 words) and title-cased.
    """
    m = INLINE_TITLE_PATTERN.match(text)
    if not m:
        return False
    title_part = m.group(1).strip()
    words = title_part.split()
    if len(words) > 6:
        return False
    # Title must be mostly capitalized words (not a sentence)
    cap_words = sum(1 for w in words if w[:1].isupper() or not w[:1].isalpha())
    return cap_words / len(words) >= 0.6


def split_inline_title(text: str):
    """Split 'ProjectName - description' into (title, description)."""
    m = INLINE_TITLE_PATTERN.match(text)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return "", text


def split_title_line(line: str):
    """Split 'Title — Tech Stack' or 'Title | Tech | Date' plain lines."""
    duration = ""
    remainder = line

    dm = DATE_RANGE_PATTERN.search(line)
    if dm and (dm.end() - dm.start()) >= 4:
        duration = dm.group(0).strip()
        remainder = (line[: dm.start()] + line[dm.end():]).strip(" |,-–—")

    parts = [p.strip() for p in TITLE_SEP.split(remainder) if p.strip()]
    if len(parts) >= 2:
        return parts[0], ", ".join(parts[1:]).strip(", "), duration
    elif parts:
        return parts[0], "", duration
    return remainder.strip(), "", duration


def new_project(title="", tech="", duration=""):
    return {
        "title": title,
        "tech_stack": tech,
        "duration": duration,
        "links": [],
        "description": [],
    }


def merge_wrapped_lines(raw_lines):
    """
    Pass 1: collapse hard-wrapped physical lines into logical lines.
    Returns list of ["bullet"|"plain", text].
    """
    merged = []

    for line in raw_lines:
        if is_bullet(line):
            merged.append(["bullet", strip_bullet_marker(line)])
            continue

        if merged:
            prev_kind, prev_text = merged[-1]

            # Bullet that hasn't ended → continuation
            if prev_kind == "bullet" and not ends_sentence(prev_text):
                merged[-1][1] = (prev_text + " " + line).strip()
                continue

            # Plain that ended with comma/connector → continuation
            if prev_kind == "plain" and ends_with_open(prev_text):
                merged[-1][1] = (prev_text + " " + line).strip()
                continue

            # Line starts lowercase/digit → always continuation
            if starts_like_continuation(line):
                merged[-1][1] = (prev_text + " " + line).strip()
                continue

        merged.append(["plain", line])

    return merged


def extract_projects(sections: dict) -> list:
    text = (
        sections.get("projects", "")
        or sections.get("personal projects", "")
        or sections.get("academic projects", "")
    )
    if not text:
        return []

    raw = [clean_line(l) for l in text.split("\n")]
    raw = [l for l in raw if l]

    # Hard stop at next section header
    for idx, l in enumerate(raw):
        if is_section_header(l):
            raw = raw[:idx]
            break

    logical = merge_wrapped_lines(raw)

    projects = []
    current = None

    # Detect format: are ALL logical lines bullets with no plain title lines?
    plain_lines = [t for k, t in logical if k == "plain"]
    bullet_lines = [t for k, t in logical if k == "bullet"]
    all_bullets_format = (
        len(bullet_lines) > 0
        and len(plain_lines) == 0
        and all(is_inline_titled_bullet(b) for b in bullet_lines)
    )

    if all_bullets_format:
        # Format: each bullet is its own project "Title - description"
        for _, text_line in logical:
            title, desc = split_inline_title(text_line)
            proj = new_project(title=title)
            if desc:
                proj["description"].append(desc)
            proj["links"].extend(LINK_PATTERN.findall(text_line))
            projects.append(proj)
        return projects

    # Mixed / standard format
    for kind, text_line in logical:
        if not text_line:
            continue

        if kind == "bullet":
            # Check if this bullet itself is "Title - description" style
            # even in a mixed-format resume
            if is_inline_titled_bullet(text_line) and (
                current is None or not current["description"]
            ):
                if current is not None and current["title"]:
                    projects.append(current)
                title, desc = split_inline_title(text_line)
                current = new_project(title=title)
                if desc:
                    current["description"].append(desc)
                current["links"].extend(LINK_PATTERN.findall(text_line))
                continue

            if current is None:
                current = new_project()
            cleaned = LINK_PATTERN.sub("", text_line).strip()
            if TECH_LABEL_PATTERN.match(cleaned):
                extra = TECH_LABEL_PATTERN.sub("", cleaned).strip(" :-")
                current["tech_stack"] = (
                    (current["tech_stack"] + ", " if current["tech_stack"] else "") + extra
                )
            elif cleaned:
                current["description"].append(cleaned)
            current["links"].extend(LINK_PATTERN.findall(text_line))
            continue

        # plain line → new project title block
        if current is not None and not current["description"]:
            if TECH_LABEL_PATTERN.match(text_line):
                extra = TECH_LABEL_PATTERN.sub("", text_line).strip(" :-")
                current["tech_stack"] = (
                    (current["tech_stack"] + ", " if current["tech_stack"] else "") + extra
                )
                continue
            if DATE_LINE_PATTERN.match(text_line.strip()):
                current["duration"] = current["duration"] or text_line
                continue
            if len(text_line.split()) <= 3 and not TITLE_SEP.search(text_line):
                current["links"].extend(LINK_PATTERN.findall(text_line))
                continue

        if current is not None:
            projects.append(current)

        title, tech, duration = split_title_line(text_line)
        current = new_project(
            title=title.strip(" –—|"),
            tech=tech.strip(", –—|"),
            duration=duration,
        )
        current["links"].extend(LINK_PATTERN.findall(text_line))

    if current is not None:
        projects.append(current)

    # Dedupe links, drop empty shells
    result = []
    for proj in projects:
        seen: set = set()
        proj["links"] = [l for l in proj["links"] if not (l in seen or seen.add(l))]
        if proj["title"] or proj["description"]:
            result.append(proj)

    return result