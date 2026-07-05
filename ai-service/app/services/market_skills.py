from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum

import pandas as pd


class SkillTier(str, Enum):
    CORE = "core"
    IMPORTANT = "important"
    NICE_TO_HAVE = "nice_to_have"


TIER_WEIGHTS = {
    SkillTier.CORE: 3,
    SkillTier.IMPORTANT: 2,
    SkillTier.NICE_TO_HAVE: 1,
}

TIER_THRESHOLDS = {
    SkillTier.CORE: 0.50,
    SkillTier.IMPORTANT: 0.20,
    SkillTier.NICE_TO_HAVE: 0.05,
}

SKILL_ALIASES = {
    "ml": "machine learning",
    "machine-learning": "machine learning",
    "machine_learning": "machine learning",

    "ai": "artificial intelligence",

    "py": "python",
    "python3": "python",

    "sql server": "sql",
    "mysql": "sql",
    "postgresql": "sql",
    "postgres": "sql",

    "pandas library": "pandas",

    "tf": "tensorflow",

    "scikit learn": "scikit-learn",
    "sklearn": "scikit-learn",

    "k8s": "kubernetes",

    "js": "javascript",

    "nlp": "natural language processing",

    "cv": "computer vision"
}


def normalize_skill(raw: str) -> str:
    s = raw.strip().lower()
    return SKILL_ALIASES.get(s, s)


@dataclass
class SkillStat:
    skill: str
    frequency: int
    coverage: float
    tier: SkillTier


@dataclass
class MarketSkillProfile:
    role: str
    total_postings: int
    skills: dict[str, SkillStat] = field(default_factory=dict)

    def tiered(self, tier: SkillTier) -> list[SkillStat]:
        return sorted(
            (s for s in self.skills.values() if s.tier == tier),
            key=lambda s: s.coverage,
            reverse=True,
        )

    def total_weight(self) -> int:
        return sum(TIER_WEIGHTS[s.tier] for s in self.skills.values())


def filter_postings_by_role(df: pd.DataFrame, target_role: str) -> pd.DataFrame:
    role = target_role.lower().strip()
    title_match = df["title"].str.lower().str.contains(role, regex=False, na=False)
    category_match = df["category"].str.lower().str.contains(role, regex=False, na=False)
    return df[title_match | category_match]


def build_market_skill_profile(
    df: pd.DataFrame,
    target_role: str,
    min_coverage: float = TIER_THRESHOLDS[SkillTier.NICE_TO_HAVE],
) -> MarketSkillProfile:
    postings = filter_postings_by_role(df, target_role)
    total = len(postings)

    if total == 0:
        return MarketSkillProfile(role=target_role, total_postings=0)

    skill_counts: dict[str, int] = {}
    for raw_skills in postings["skills"].dropna():
        seen_in_posting = {
            normalize_skill(s) for s in raw_skills.split(",") if s.strip()
        }
        for skill in seen_in_posting:
            skill_counts[skill] = skill_counts.get(skill, 0) + 1

    profile = MarketSkillProfile(role=target_role, total_postings=total)
    for skill, count in skill_counts.items():
        coverage = count / total
        if coverage < min_coverage:
            continue
        tier = _assign_tier(coverage)
        profile.skills[skill] = SkillStat(
            skill=skill, frequency=count, coverage=coverage, tier=tier
        )

    return profile


def _assign_tier(coverage: float) -> SkillTier:
    if coverage >= TIER_THRESHOLDS[SkillTier.CORE]:
        return SkillTier.CORE
    if coverage >= TIER_THRESHOLDS[SkillTier.IMPORTANT]:
        return SkillTier.IMPORTANT
    return SkillTier.NICE_TO_HAVE


from pathlib import Path

DATASET_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "master_jobs.csv"
)

df = pd.read_csv(DATASET_PATH)

profile = build_market_skill_profile(df, "Data Scientist")

print(f"Total postings: {profile.total_postings}\n")

for skill in ["python", "sql", "machine learning", "pandas", "docker"]:
    if skill in profile.skills:
        s = profile.skills[skill]
        print(
            f"{skill:<20}"
            f"coverage={s.coverage:.2%}   "
            f"freq={s.frequency}   "
            f"tier={s.tier.value}"
        )
    else:
        print(f"{skill:<20} NOT FOUND")