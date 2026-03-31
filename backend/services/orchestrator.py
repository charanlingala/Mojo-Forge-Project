import asyncio
from agents.planner_agent import run_planner_agent
from agents.frontend_agent import run_frontend_agent
from agents.backend_agent import run_backend_agent
from agents.qa_agent import run_qa_agent
from agents.reviewer_agent import run_reviewer_agent
from services.file_writer import write_output

async def run_orchestration(idea: str) -> dict:
    prd = await run_planner_agent(idea)

    ui_plan, api_spec, test_cases = await asyncio.gather(
        run_frontend_agent(idea, prd),
        run_backend_agent(idea, prd),
        run_qa_agent(idea, prd),
    )

    review_report = await run_reviewer_agent(prd, ui_plan, api_spec, test_cases)

    write_output("prd.md", prd)
    write_output("ui_plan.md", ui_plan)
    write_output("api_spec.md", api_spec)
    write_output("test_cases.md", test_cases)
    write_output("review_report.md", review_report)

    return {
        "idea": idea,
        "prd": prd,
        "ui_plan": ui_plan,
        "api_spec": api_spec,
        "test_cases": test_cases,
        "review_report": review_report,
    }