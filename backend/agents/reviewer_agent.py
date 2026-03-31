from services.llm_client import generate_text
from services.prompt_loader import load_prompt

async def run_reviewer_agent(prd: str, ui_plan: str, api_spec: str, test_cases: str) -> str:
    system_role = "You are a Reviewer Agent."
    template = load_prompt("reviewer.txt")
    prompt = template.format(
        prd=prd,
        ui_plan=ui_plan,
        api_spec=api_spec,
        test_cases=test_cases
    )
    return await generate_text(system_role, prompt)