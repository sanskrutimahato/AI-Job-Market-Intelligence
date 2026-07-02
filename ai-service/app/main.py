from fastapi import FastAPI
from app.routes.resume_routes import router as resume_router

app = FastAPI(
    title="AI Resume Parser API",
    version="1.0.0"
)

app.include_router(
    resume_router,
    prefix="/api",
    tags=["Resume Parser"]
)


@app.get("/")
def root():
    return {
        "message": "AI Resume Parser API is Running"
    }