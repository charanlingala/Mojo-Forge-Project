import type { AgentStep } from "@/types"

type Props = {
  steps: AgentStep[]
}

export default function AgentStatus({ steps }: Props) {
  return (
    <div className="statusCard">
      <h2 style={{ marginBottom: "16px" }}>Agent Progress</h2>
      <div className="statusList">
        {steps.map((step) => (
          <div key={step.name} className="statusItem">
            <span>{step.name}</span>
            <span className={`badge ${step.status}`}>{step.status}</span>
          </div>
        ))}
      </div>
    </div>
  )
}