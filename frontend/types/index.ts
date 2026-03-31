export type GenerateResponse = {
  idea: string
  prd: string
  ui_plan: string
  api_spec: string
  test_cases: string
  review_report: string
}

export type AgentStep = {
  name: string
  status: "pending" | "running" | "done"
}