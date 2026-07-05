from __future__ import annotations
from dataclasses import dataclass

from .market_skills import MarketSkillProfile, SkillTier, TIER_WEIGHTS, normalize_skill


@dataclass
class SkillGap:
    skill: str
    tier: SkillTier
    coverage: float


@dataclass
class ATSResult:
    ats_score: float
    matched_skills: dict[SkillTier, list[str]]
    missing_skills: list[SkillGap]
    total_market_skills_considered: int


class ATSScoreEngine:
    def score(
        self, resume_skills: list[str], market_profile: MarketSkillProfile
    ) -> ATSResult:
        normalized_resume = {normalize_skill(s) for s in resume_skills}

        matched_weight = 0
        matched_by_tier: dict[SkillTier, list[str]] = {tier: [] for tier in SkillTier}
        missing: list[SkillGap] = []

        for stat in market_profile.skills.values():
            weight = TIER_WEIGHTS[stat.tier]
            if stat.skill in normalized_resume:
                matched_weight += weight
                matched_by_tier[stat.tier].append(stat.skill)
            else:
                missing.append(
                    SkillGap(skill=stat.skill, tier=stat.tier, coverage=stat.coverage)
                )

        total_weight = market_profile.total_weight()
        score = (matched_weight / total_weight * 100) if total_weight else 0.0

        missing.sort(key=lambda g: (TIER_WEIGHTS[g.tier], g.coverage), reverse=True)

        return ATSResult(
            ats_score=round(score, 2),
            matched_skills=matched_by_tier,
            missing_skills=missing,
            total_market_skills_considered=len(market_profile.skills),
        )


class MarketReadinessEngine:
    """
    Rewards breadth of coverage across tiers rather than raw overlap.
    A candidate who has all core skills but no nice-to-haves still
    scores well; one who only has scattered nice-to-haves does not.
    """

    def score(self, ats_result: ATSResult, market_profile: MarketSkillProfile) -> float:
        tier_coverage: dict[SkillTier, float] = {}
        for tier in SkillTier:
            total_in_tier = len(market_profile.tiered(tier))
            matched_in_tier = len(ats_result.matched_skills.get(tier, []))
            tier_coverage[tier] = (
                matched_in_tier / total_in_tier if total_in_tier else 0.0
            )

        weighted = (
            tier_coverage[SkillTier.CORE] * 0.6
            + tier_coverage[SkillTier.IMPORTANT] * 0.3
            + tier_coverage[SkillTier.NICE_TO_HAVE] * 0.1
        )
        return round(weighted * 100, 2)


if __name__ == "__main__":
    from .market_skills import SkillStat

    profile = MarketSkillProfile(
        role="Data Scientist",
        total_postings=10,
        skills={
            "python": SkillStat("python", 9, 0.90, SkillTier.CORE),
            "sql": SkillStat("sql", 8, 0.80, SkillTier.CORE),
            "machine learning": SkillStat("machine learning", 7, 0.70, SkillTier.CORE),
            "pandas": SkillStat("pandas", 4, 0.40, SkillTier.IMPORTANT),
            "docker": SkillStat("docker", 3, 0.30, SkillTier.IMPORTANT),
            "kubernetes": SkillStat("kubernetes", 1, 0.10, SkillTier.NICE_TO_HAVE),
        },
    )

    resume_skills = ["Python", "SQL", "Machine Learning", "Pandas", "Docker"]

    score_engine = ATSScoreEngine()
    result = score_engine.score(resume_skills, profile)

    print(f"ATS Score: {result.ats_score}%")
    print(f"Matched: {result.matched_skills}")
    print(f"Missing: {[g.skill for g in result.missing_skills]}\n")

    readiness_engine = MarketReadinessEngine()
    readiness = readiness_engine.score(result, profile)
    print(f"Market Readiness Score: {readiness}%")

    # 5 of 6 skills matched, only "kubernetes" missing -> score should be high, not ~0.4%
    assert result.ats_score > 80
    assert "kubernetes" in [g.skill for g in result.missing_skills]
    print("All assertions passed.")