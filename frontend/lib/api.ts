import type { GenerateResponse } from "@/types"

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"

export async function generateBuildPlan(idea: string): Promise<GenerateResponse> {
  const response = await fetch(`${API_URL}/generate`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ idea })
  })

  if (!response.ok) {
    throw new Error("Failed to generate build plan")
  }

  return response.json()
}