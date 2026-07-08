from fastapi import APIRouter, UploadFile, File, HTTPException  # type: ignore[import]
import shutil
import os

from app.services.resume_parser import parse_resume

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/parseResume")
async def parse_resume_api(file: UploadFile = File(...)):
    """
    Upload a resume PDF and return parsed information.
    """

    # Validate file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    try:
        # Save uploaded file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Parse resume
        parsed_data = parse_resume(file_path)

        return {
            "success": True,
            "message": "Resume parsed successfully.",
            "data": parsed_data
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )

    # finally:
    #     # Delete uploaded file after parsing
    #     if os.path.exists(file_path):
    #         os.remove(file_path)