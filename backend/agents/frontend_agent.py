from services.llm_client import generate_text
from services.prompt_loader import load_prompt

async def run_frontend_agent(idea: str, prd: str) -> str:
    system_role = "You are a Frontend Architect Agent."
    template = load_prompt("frontend.txt")
    prompt = template.format(idea=idea, prd=prd)
    return await generate_text(system_role, prompt)