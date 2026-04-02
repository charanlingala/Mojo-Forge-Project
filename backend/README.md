# MoJoForge Backend

MoJoForge Backend is the core engine of the project that converts a simple product idea into a structured development plan using multiple AI agents.

Instead of treating the input like a normal chatbot request, the backend breaks the idea into clear stages such as requirements, UI design, backend planning, and testing. Each stage is handled by a dedicated agent, which makes the output more organized and closer to how real teams work.

The goal of this backend is simple — take a vague idea and turn it into something developers can actually start building.

---

# What This Backend Does

When a user provides a product idea, the backend:

- Creates a Product Requirement Document (PRD)
- Generates a UI/Frontend plan
- Designs Backend architecture and APIs
- Produces Test cases
- Reviews the overall output for improvements

All results are saved as structured files so they can be directly used for development.

---

# Project Structure


backend/
├── agents/
│   ├── planner_agent.py
│   ├── frontend_agent.py
│   ├── backend_agent.py
│   ├── qa_agent.py
│   └── reviewer_agent.py
│
├── services/
│   ├── llm_client.py
│   ├── orchestrator.py
│   ├── file_writer.py
│   └── prompt_loader.py
│
├── prompts/
│   ├── planner.txt
│   ├── frontend.txt
│   ├── backend.txt
│   ├── qa.txt
│   └── reviewer.txt
│
├── outputs/
│   ├── prd.md
│   ├── ui_plan.md
│   ├── api_spec.md
│   ├── test_cases.md
│   └── review_report.md
│
└── README.md



How the Backend Works
The flow is straightforward:
1. User provides a product idea
2. The Orchestrator controls execution
3. Agents run in sequence:
   Planner Agent → Generates PRD
   Frontend Agent → Creates UI plan
   Backend Agent → Designs APIs and system
   QA Agent → Writes test cases
   Reviewer Agent → Reviews and improves output
4. Final results are saved in the outputs/ folder
This step-by-step approach ensures the output is structured and useful, not just generated text.

Key Components
Agents
Each agent handles a specific responsibility. This separation makes the system clean and scalable.

Orchestrator
Controls the flow and ensures each agent receives the right input.

LLM Client
Handles communication with the AI model.

Prompt Loader
Loads prompts from files, making it easy to update behavior without changing code.

File Writer
Stores all generated outputs into readable markdown files.

Technologies Used
Python
LLM API (OpenAI or similar)
Modular architecture
Markdown file generation


Setup Instructions
1. Clone the repository
git clone <your-repo-url>
cd MoJoForge/backend

2. Create virtual environment
python -m venv venv

3. Activate environment
Windows:  venv\Scripts\activate

4. Install dependencies
pip install -r requirements.txt

Environment Configuration
Create a .env file inside the backend folder:
OPENAI_API_KEY=your_api_key_here
MODEL_NAME=gpt-4o-mini

Running the Backend
python main.py
After running, check the outputs/ folder for generated files.

Example Input
Build an app that helps users track daily expenses and provides smart saving suggestions.

Example Output
The backend generates:
prd.md → Product requirements
ui_plan.md → UI structure
api_spec.md → Backend/API design
test_cases.md → Test scenarios
review_report.md → Quality review

Why This Project Stands Out
This project demonstrates:
Multi-agent architecture
Clear separation of responsibilities
Practical use of AI in real workflows
Ability to convert ideas into actionable plans
Instead of generating random content, it produces structured outputs that can be directly used by developers.

Future Enhancements
Add FastAPI endpoints
Store results in a database
Add user interface
Support multiple AI models
Improve agent collaboration

Summary
MoJoForge Backend shows how AI can be used beyond chat — as a system that organizes, plans, and prepares real development work.
It is simple in design, but powerful in execution, making it a strong project for both learning and real-world use.
