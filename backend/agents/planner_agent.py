from services.llm_client import generate_text
from services.prompt_loader import load_prompt

async def run_planner_agent(idea: str) -> str:
    system_role = "You are a Product Planner Agent."
    template = load_prompt("planner.txt")
    prompt = template.format(idea=idea)
    return await generate_text(system_role, prompt)