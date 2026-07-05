from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

from app.services.ats_engine import ats_engine

router = APIRouter()


class ATSRequest(BaseModel):
    target_role: str
    resume_skills: List[str]


@router.post("/atsScore")
def calculate_ats_score(request: ATSRequest):
    try:
        report = ats_engine.evaluate(
            resume_skills=request.resume_skills,
            target_role=request.target_role,
        )

        return {
            "role": report.role,
            "total_postings_analyzed": report.total_postings_analyzed,
            "ats_score": report.ats_score,
            "market_readiness_score": report.market_readiness_score,
            "matched_skills": report.matched_skills,
            "missing_skills": report.missing_skills,
            "total_market_skills_considered": report.total_market_skills_considered,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )