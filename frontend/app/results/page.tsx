import IdeaForm from "@/components/IdeaForm"

export default function HomePage() {
  return (
    <main className="page">
      <div className="container">
        <div className="hero">
          <h1>MoJoForge</h1>
          <p>
            Turn one plain-English idea into a structured build plan using
            <strong> multi-agent orchestration</strong>.
          </p>
        </div>
        <IdeaForm />
      </div>
    </main>
  )
}