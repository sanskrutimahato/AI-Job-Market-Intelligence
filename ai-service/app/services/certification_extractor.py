import re


BULLET_CHARS = "•◦▪‣⁃●○*"
DASH_BULLET = re.compile(r"^[–—\-]\s+")
NUMBERED_PATTERN = re.compile(r"^\s*\d+[\.\)]\s+")

MONTHS = r"(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?"
DATE_TOKEN = rf"({MONTHS}\s*\d{{4}}|\d{{1,2}}/\d{{4}}|\d{{4}})"
DATE_PATTERN = re.compile(DATE_TOKEN, re.IGNORECASE)
DATE_LINE_PATTERN = re.compile(
    rf"^\s*{DATE_TOKEN}\s*([-–—]|to)\s*{DATE_TOKEN}\s*$|^\s*{DATE_TOKEN}\s*$",
    re.IGNORECASE,
)

SECTION_STOP_WORDS = [
    "contact", "education", "skills", "experience", "work experience",
    "professional experience", "projects", "summary", "objective",
    "references", "languages", "interests", "publications", "hobbies",
    "declaration", "extracurricular", "volunteer", "leadership",
]

KNOWN_ISSUERS = [
    "coursera", "udemy", "edx", "linkedin", "google", "microsoft", "aws",
    "amazon", "oracle", "ibm", "cisco", "meta", "facebook", "apple",
    "infosys", "tcs", "wipro", "nasscom", "nptel", "swayam", "nvidia",
    "deeplearning.ai", "udacity", "simplilearn", "great learning",
    "pluralsight", "hackerrank", "hackerearth", "leetcode", "codecademy",
    "github", "jetbrains", "adobe", "salesforce", "tableau", "autodesk",
    "red hat", "comptia", "pmi", "isc2", "isaca", "ec-council", "certiport",
    "ieee", "acm", "mit", "stanford", "harvard", "coursera", "edx",
]

INLINE_SEP = re.compile(r"\s*[–—|]\s*")


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
    if DASH_BULLET.match(line) and len(line.split()) >= 2:
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


def extract_date(text: str) -> str:
    m = DATE_PATTERN.search(text)
    return m.group(0).strip() if m else ""


def is_date_only(line: str) -> bool:
    return bool(DATE_LINE_PATTERN.match(line.strip()))


def is_issuer_line(line: str) -> bool:
    lower = line.lower()
    return any(issuer in lower for issuer in KNOWN_ISSUERS)


def ends_with_open(text: str) -> bool:
    t = text.rstrip()
    if not t:
        return False
    if t.endswith(","):
        return True
    last = t.split()[-1].lower().strip(",")
    return last in {"and", "or", "&", "by", "from", "via", "through"}


def starts_like_continuation(line: str) -> bool:
    if not line:
        return False
    if line[0].islower():
        return True
    first = line.split()[0].lower().strip(",.;:")
    return first in {"and", "or", "&", "with", "by", "from"}


def merge_wrapped_lines(raw_lines):
    merged = []
    for line in raw_lines:
        bullet = is_bullet(line)
        text = strip_bullet_marker(line) if bullet else line
        kind = "bullet" if bullet else "plain"

        if merged:
            prev_kind, prev_text = merged[-1]
            if ends_with_open(prev_text) or starts_like_continuation(text):
                merged[-1][1] = (prev_text + " " + text).strip()
                continue

        merged.append([kind, text])
    return merged


def parse_inline_cert(text: str):
    """
    Parse formats like:
      'Oracle – Certified Generative AI Professional'
      'Coursera – Database Structures and Management with MySQL'
      'Merit Scholarship – Achieved perfect 10.0 CGPA'
      'AWS Certified Developer – Amazon | Jan 2023'
    Returns (name, issuer, year).
    """
    name, issuer, year = text, "", ""

    dm = DATE_PATTERN.search(text)
    if dm:
        year = dm.group(0).strip()
        text = (text[: dm.start()] + text[dm.end():]).strip(" |,-–—")

    parts = [p.strip() for p in INLINE_SEP.split(text) if p.strip()]

    if len(parts) >= 2:
        left = parts[0]
        right = " ".join(parts[1:])

        left_is_issuer = is_issuer_line(left)
        right_is_issuer = is_issuer_line(right)

        if left_is_issuer and not right_is_issuer:
            issuer = left
            name = right
        elif right_is_issuer and not left_is_issuer:
            name = left
            issuer = right
        else:
            # Neither or both match known issuers:
            # treat shorter left as issuer if it's ≤3 words
            if len(left.split()) <= 3:
                issuer = left
                name = right
            else:
                name = left
                issuer = right
    elif parts:
        name = parts[0]

    return name.strip(" –—|"), issuer.strip(" –—|"), year


def new_cert(name="", issuer="", year=""):
    return {"name": name, "issuer": issuer, "year": year}


def extract_certifications(sections: dict) -> list:
    # Collect text from ALL cert/achievement-related keys
    candidate_keys = [
        "certifications", "certificates", "achievements",
        "certifications & awards", "awards & certifications",
        "certifications and awards", "certifications & achievements",
        "achievements & certifications", "licenses",
        "courses", "training", "professional development",
    ]

    texts = []
    for key in sections:
        key_lower = key.lower().strip()
        if any(ck in key_lower for ck in [
            "certif", "award", "achiev", "license",
            "course", "training", "scholarship"
        ]):
            texts.append(sections[key])

    # Fallback: nothing matched above
    if not texts:
        for key in candidate_keys:
            if sections.get(key):
                texts.append(sections[key])

    if not texts:
        return []

    combined = "\n".join(texts)

    raw = [clean_line(l) for l in combined.split("\n")]
    raw = [l for l in raw if l]

    # Hard stop at next unrelated section header
    for idx, l in enumerate(raw):
        if is_section_header(l):
            raw = raw[:idx]
            break

    logical = merge_wrapped_lines(raw)

    certifications = []
    pending = None

    for kind, line in logical:
        if not line:
            continue

        has_sep = bool(INLINE_SEP.search(line))
        has_date = bool(DATE_PATTERN.search(line))
        has_issuer = is_issuer_line(line)

        # Self-contained line: has separator OR known issuer
        if has_sep or has_issuer:
            if pending:
                certifications.append(pending)
                pending = None
            name, issuer, year = parse_inline_cert(line)
            if name:
                certifications.append(new_cert(name=name, issuer=issuer, year=year))
            continue

        # Date-only line
        if is_date_only(line):
            if pending:
                pending["year"] = pending["year"] or extract_date(line)
            continue

        # Line with inline date but no separator and no known issuer
        if has_date:
            year = extract_date(line)
            name = DATE_PATTERN.sub("", line).strip(" –—|,")
            if pending:
                pending["year"] = pending["year"] or year
                if name:
                    pending["name"] = pending["name"] or name
                certifications.append(pending)
                pending = None
            else:
                certifications.append(new_cert(name=name, year=year))
            continue

        # Plain name line
        if pending:
            certifications.append(pending)
        pending = new_cert(name=line)

    if pending:
        certifications.append(pending)

    return [c for c in certifications if c["name"].strip() or c["issuer"].strip()]