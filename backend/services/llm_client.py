import os
from dotenv import load_dotenv

load_dotenv()

APP_MODE = os.getenv("APP_MODE", "mock").strip().lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()

def _mock_response(system_role: str, user_prompt: str) -> str:
    if "Product Planner Agent" in system_role:
        return f"""# Product Requirements Document

## Product Title
AI-generated product for: {user_prompt[:80]}

## Problem Statement
Users need a faster way to turn an idea into a structured implementation plan.

## Target Users
- Founders
- Developers
- Product teams

## Core Features
- Input a product idea
- Generate a PRD
- Generate UI plan
- Generate API plan
- Generate QA scenarios

## User Stories
- As a user, I want to submit an idea and receive a build-ready outline.
- As a developer, I want clear specs to reduce planning time.

## Non-Goals
- Full production deployment
- Authentication for all enterprise roles

## Success Metrics
- Faster planning time
- Better handoff quality
- Clearer implementation scope

## MVP Scope
Single input box, orchestration backend, generated output sections.
"""

    if "Frontend Architect Agent" in system_role:
        return """# UI Plan

## Pages
- Home page
- Results page

## Key Components
- Idea input form
- Generate button
- Agent progress tracker
- Output cards

## Form Fields
- Product idea text area

## Validation Rules
- Input cannot be empty
- Show error if empty

## User Interactions
- Enter idea
- Click generate
- See progress
- View results

## Suggested Component Hierarchy
- Page
  - Hero section
  - IdeaForm
  - AgentStatus
  - OutputCard list
"""

    if "Backend Architect Agent" in system_role:
        return """# API Spec

## Entities
- IdeaRequest
- GeneratedPlan

## API Endpoints
### POST /generate
Request:
{
  "idea": "Build a task manager for students"
}

Response:
{
  "idea": "...",
  "prd": "...",
  "ui_plan": "...",
  "api_spec": "...",
  "test_cases": "...",
  "review_report": "..."
}

## Validation Logic
- idea is required
- idea must not be blank

## Suggested Data Model
- idea: string
- prd: text
- ui_plan: text
- api_spec: text
- test_cases: text
- review_report: text

## Business Rules
- Planner runs first
- Frontend, backend, and QA run in parallel
- Reviewer runs last
"""

    if "QA Agent" in system_role:
        return """# Test Cases

## Functional Tests
1. User enters valid idea and gets generated outputs
2. User sees agent progress updates
3. Results page displays all sections

## Negative Tests
1. Empty input should show validation error
2. API failure should show user-friendly error

## Validation Scenarios
- Whitespace-only input
- Very short idea
- Very long idea

## Edge Cases
- Network timeout
- Partial agent failure

## Acceptance Criteria
- All five output sections are returned
- UI handles loading and error states
"""

    if "Reviewer Agent" in system_role:
        return """# Review Report

## Summary
The generated outputs are aligned for MVP delivery.

## Issues Found
- Authentication not defined
- Persistence layer is optional and not included in MVP
- Error handling can be expanded

## Fix Recommendations
- Add retry logic
- Add persistent storage for history
- Add authentication in future version
"""

    return "No mock response available."

async def generate_text(system_role: str, user_prompt: str) -> str:
    if APP_MODE == "mock" or not OPENAI_API_KEY:
        return _mock_response(system_role, user_prompt)

    from openai import AsyncOpenAI

    client = AsyncOpenAI(api_key=OPENAI_API_KEY)

    response = await client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_role},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.7,
    )

    return response.choices[0].message.content or ""