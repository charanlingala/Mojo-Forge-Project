"use client"

import { useState } from "react"
import { useRouter } from "next/navigation"
import { generateBuildPlan } from "@/lib/api"
import AgentStatus from "@/components/AgentStatus"
import type { AgentStep, GenerateResponse } from "@/types"

const createInitialSteps = (): AgentStep[] => [
  { name: "Planner Agent", status: "pending" },
  { name: "Frontend Agent", status: "pending" },
  { name: "Backend Agent", status: "pending" },
  { name: "QA Agent", status: "pending" },
  { name: "Reviewer Agent", status: "pending" }
]

export default function IdeaForm() {
  const [idea, setIdea] = useState("")
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")
  const [steps, setSteps] = useState<AgentStep[]>(createInitialSteps())
  const router = useRouter()

  const updateStep = (index: number, status: AgentStep["status"]) => {
    setSteps((prev) =>
      prev.map((step, i) => (i === index ? { ...step, status } : step))
    )
  }

  const handleGenerate = async () => {
    if (!idea.trim()) {
      setError("Please enter a product idea.")
      return
    }

    setLoading(true)
    setError("")
    setSteps(createInitialSteps())

    try {
      updateStep(0, "running")
      await new Promise((resolve) => setTimeout(resolve, 500))
      updateStep(0, "done")

      updateStep(1, "running")
      updateStep(2, "running")
      updateStep(3, "running")

      const data: GenerateResponse = await generateBuildPlan(idea)

      updateStep(1, "done")
      updateStep(2, "done")
      updateStep(3, "done")

      updateStep(4, "running")
      await new Promise((resolve) => setTimeout(resolve, 400))
      updateStep(4, "done")

      sessionStorage.setItem("mojoforge_result", JSON.stringify(data))
      router.push("/results")
    } catch {
      setError("Something went wrong while generating the build plan.")
    } finally {
      setLoading(false)
    }
  }

  return (
    <>
      <div className="formCard">
        <textarea
          className="textarea"
          placeholder="Enter your product idea"
          value={idea}
          onChange={(e) => setIdea(e.target.value)}
        />
        <button
          className="primaryButton"
          onClick={handleGenerate}
          disabled={loading}
        >
          {loading ? "Generating..." : "Generate Build Plan"}
        </button>
        {error && <p className="errorText">{error}</p>}
      </div>

      <AgentStatus steps={steps} />
    </>
  )
}