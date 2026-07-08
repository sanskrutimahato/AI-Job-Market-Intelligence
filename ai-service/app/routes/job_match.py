import os
import shutil

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.pdf_parser import extract_text_from_pdf
from app.services.job_match_engine import calculate_job_match

router = APIRouter()


@router.post("/jobMatch")
async def job_match(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    """
    Upload a resume PDF and compare it with a job description.
    """

    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, resume.filename)

    try:
        # Save uploaded PDF
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(resume.file, buffer)

        # Extract text from PDF
        resume_text = extract_text_from_pdf(file_path)

        # Calculate job match
        result = calculate_job_match(
            resume_text=resume_text,
            job_description=job_description
        )

        return {
            "success": True,
            "message": "Job match calculated successfully.",
            "data": result
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Job match failed: {str(e)}"
        )

    finally:
        # Delete uploaded file
        try:
            resume.file.close()

            if os.path.exists(file_path):
                os.remove(file_path)

        except Exception:
            pass