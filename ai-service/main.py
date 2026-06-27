from fastapi import FastAPI

app = FastAPI(
    title="AI Job Market Intelligence API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "AI Service Running"
    }