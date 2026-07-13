from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from app.routes.resume_routes import router as resume_router
from app.routes.ats import router as ats_router
from app.routes.job_match import router as job_match_router

app = FastAPI(
    title="AI Resume Parser API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Resume Parser Routes
app.include_router(
    resume_router,
    prefix="/api",
    tags=["Resume Parser"]
)

# ATS Score Routes
app.include_router(
    ats_router,
    prefix="/api",
    tags=["ATS Score"]
)

# Job Match Routes
app.include_router(
    job_match_router,
    prefix="/api",
    tags=["Job Match"]
)

@app.get("/")
def root():
    return {
        "message": "AI Resume Parser API is Running"
    }