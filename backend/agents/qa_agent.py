from services.llm_client import generate_text
from services.prompt_loader import load_prompt

async def run_qa_agent(idea: str, prd: str) -> str:
    system_role = "You are a QA Agent."
    template = load_prompt("qa.txt")
    prompt = template.format(idea=idea, prd=prd)
    return await generate_text(system_role, prompt)