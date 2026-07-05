import re


def clean_skill(skill: str) -> str:
    """
    Clean a single skill string.
    """

    skill = skill.lower().strip()

    # Remove extra spaces
    skill = re.sub(r"\s+", " ", skill)

    return skill


def clean_skill_list(skills):
    """
    Clean and remove duplicate skills.
    """

    cleaned = []

    for skill in skills:

        skill = clean_skill(skill)

        if skill and skill not in cleaned:
            cleaned.append(skill)

    return cleaned
if __name__ == "__main__":

    sample = [
        " Python ",
        "SQL",
        "python",
        " Machine Learning ",
        "sql"
    ]

    print(clean_skill_list(sample))