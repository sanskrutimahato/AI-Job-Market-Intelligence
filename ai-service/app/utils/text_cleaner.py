import re


def clean_text(text: str) -> str:
    """
    Clean extracted resume text.

    - Remove unwanted unicode characters
    - Normalize bullets
    - Merge broken words
    - Remove extra spaces
    - Remove empty lines
    """

    # Normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Replace PDF bullets
    bullets = [
        "\uf0b7",
        "",
        "▪",
        "◦",
        "■",
        "●"
    ]

    for bullet in bullets:
        text = text.replace(bullet, "• ")

    # Replace tabs
    text = text.replace("\t", " ")

    # Remove multiple spaces
    text = re.sub(r"[ ]{2,}", " ", text)

    # Merge broken words like:
    # cross-
    # browser
    text = re.sub(r"-\n([a-z])", r"-\1", text)

    # Merge wrapped lines that are NOT headings
    lines = text.split("\n")

    cleaned = []

    for line in lines:

        line = line.strip()

        if not line:
            continue

        cleaned.append(line)

    text = "\n".join(cleaned)

    # Remove 3+ blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text