# MoJoForge – Multi-Agent AI Orchestration System

MoJoForge is a lightweight system that takes a simple product idea and turns it into a complete build plan using a **multi-agent AI workflow**.

Instead of manually figuring out requirements, UI, backend logic, and testing, this system does everything for you in one flow.

You give one input. The system gives you a structured plan.


## What problem this solves

In most projects, the toughest part is not coding — it’s planning.

Before development starts, you usually need to:

* Define requirements
* Think through UI
* Design APIs
* Handle edge cases
* Create test scenarios

This process takes time and involves multiple roles.

MoJoForge simplifies this by simulating a **team of specialized agents** that handle all of this automatically.


## What makes this different

This is not just a chatbot returning text.

The system is designed to follow a **real-world workflow**, where different roles collaborate:

* Planner Agent creates the product requirements
* Frontend Agent defines UI structure
* Backend Agent designs APIs and data models
* QA Agent generates test cases
* Reviewer Agent ensures everything is consistent

Some agents run in parallel, which makes the system faster and closer to how real teams operate.


## How the system works

The flow is simple and structured:

User enters an idea
↓
Planner Agent creates a PRD
↓
Frontend, Backend, and QA agents run in parallel
↓
Reviewer Agent validates everything
↓
Final structured output is returned


## Project structure

```
MoJoForge/
├── backend/
│   ├── agents/
│   ├── services/
│   ├── prompts/
│   ├── outputs/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── types/
│   └── package.json
│
└── README.md
```

## Frontend overview

The frontend is built using **Next.js (App Router)**.

It focuses on making the system easy to use and visually clear.

Key responsibilities:

* Accept user input (product idea)
* Trigger backend processing
* Show progress of each agent
* Display results in a structured format

Main UI sections:

* Input box for idea
* Generate button
* Agent progress tracker
* Results page with organized outputs

The frontend ensures the output is not just raw text, but something that feels like a usable product.


## Backend overview

The backend is built using **FastAPI** and handles the core logic.

Responsibilities:

* Orchestrating agents
* Running tasks in parallel
* Managing prompts
* Formatting responses

### Agents

* Planner Agent
* Frontend Agent
* Backend Agent
* QA Agent
* Reviewer Agent

### Services

* Orchestrator (controls execution flow)
* LLM client (AI or mock mode)
* Prompt loader
* File writer


## Execution flow (backend)

1. Planner Agent runs first
2. Frontend, Backend, and QA agents run in parallel using  asyncio.gather()
3. Reviewer Agent validates all outputs
4. Results are saved and returned

This setup highlights both **parallel execution** and **clear orchestration logic**.

## Mock mode vs AI mode

The system supports two modes:

**Mock Mode (default)**

* No API key required
* Returns structured sample data
* Best for demos and testing

**OpenAI Mode**

* Uses real AI responses
* Requires API key
* Generates dynamic outputs

You can switch modes in .env :

APP_MODE=mock
# or
APP_MODE=openai



## How to run the project

### Backend setup

cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn main:app --reload


Backend runs on:
[http://localhost:8000](http://localhost:8000)


### Frontend setup

cd frontend
npm install
npm run dev


Frontend runs on:
[http://localhost:3000](http://localhost:3000)


## How to test the project

### Backend testing

Open:
[http://localhost:8000/docs](http://localhost:8000/docs)

Use POST /generate with:


{
  "idea": "Build a fitness tracking app"
}



### Full flow testing

* Open frontend
* Enter a product idea
* Click “Generate Build Plan”
* View structured results


## Example output

The system generates structured sections such as:

* Product Requirements Document (PRD)
* UI plan
* API specification
* Test cases
* Review report


## What this project demonstrates

This project shows:

* Multi-agent orchestration
* Parallel execution using asyncio
* Clean separation of concerns
* Frontend and backend integration
* Workflow automation

It highlights how a single input can produce high-quality structured output.


## Why this is a strong project

This project goes beyond basic AI usage.

It demonstrates:

* System design thinking
* Real workflow automation
* Clear orchestration logic
* Practical usability

The focus is on maximizing output while reducing manual effort.


## Future improvements

Possible enhancements include:

* Export results as downloadable files
* Save history of previous runs
* Stream outputs in real-time
* Generate actual working code
* Add authentication and persistence


## Final note
This project was built to show how multiple AI agents can work together in a structured system.
The goal was to keep things simple and clear, while still demonstrating real-world problem solving.
A single idea goes in — a complete plan comes out.
