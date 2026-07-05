from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

import pandas as pd

from .market_skills import build_market_skill_profile, MarketSkillProfile
from .ats_scoring import ATSScoreEngine, MarketReadinessEngine, ATSResult


@dataclass
class ATSReport:
    role: str
    total_postings_analyzed: int
    ats_score: float
    market_readiness_score: float
    matched_skills: dict
    missing_skills: list
    total_market_skills_considered: int


class ATSEngine:
    def __init__(self, master_jobs_csv: str | Path):
        self._df = pd.read_csv(master_jobs_csv)
        self._score_engine = ATSScoreEngine()
        self._readiness_engine = MarketReadinessEngine()
        self._profile_cache: dict[str, MarketSkillProfile] = {}

    def _get_profile(self, target_role: str) -> MarketSkillProfile:
        key = target_role.lower().strip()
        if key not in self._profile_cache:
            self._profile_cache[key] = build_market_skill_profile(self._df, target_role)
        return self._profile_cache[key]

    def evaluate(self, resume_skills: list[str], target_role: str) -> ATSReport:
        profile = self._get_profile(target_role)

        if profile.total_postings == 0:
            raise ValueError(f"No postings found for role: {target_role}")

        result: ATSResult = self._score_engine.score(resume_skills, profile)
        readiness = self._readiness_engine.score(result, profile)

        return ATSReport(
            role=target_role,
            total_postings_analyzed=profile.total_postings,
            ats_score=result.ats_score,
            market_readiness_score=readiness,
            matched_skills={
                tier.value: skills for tier, skills in result.matched_skills.items()
            },
            missing_skills=[
                {
                    "skill": g.skill,
                    "tier": g.tier.value,
                    "market_coverage": round(g.coverage * 100, 1),
                }
                for g in result.missing_skills
            ],
            total_market_skills_considered=result.total_market_skills_considered,
        )

# -------------------------------
# Global Engine Instance
# -------------------------------

DATASET_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "master_jobs.csv"
)

ats_engine = ATSEngine(DATASET_PATH)
