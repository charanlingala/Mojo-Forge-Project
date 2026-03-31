from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from services.orchestrator import run_orchestration

app = FastAPI(title="MoJoForge Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class GenerateRequest(BaseModel):
    idea: str

class GenerateResponse(BaseModel):
    idea: str
    prd: str
    ui_plan: str
    api_spec: str
    test_cases: str
    review_report: str

@app.get("/")
def health_check():
    return {"message": "MoJoForge backend is running"}

@app.post("/generate", response_model=GenerateResponse)
async def generate_build_plan(request: GenerateRequest):
    result = await run_orchestration(request.idea)
    return result