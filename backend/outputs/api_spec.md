# API Spec

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
