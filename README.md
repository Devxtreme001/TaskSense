# Problem Statement

People lose context across tools and time. A task started yesterday becomes fragmented: notes in a doc, half-sent emails, partial search results, and calendar events with no agenda. That friction kills productivity and causes repeated manual work. TaskSense solves this by remembering session context, retrieving relevant past artifacts, planning multi-step work, coordinating sub-agents to fetch, rewrite, and schedule, and safely executing or staging actions for human approval. The goal is measurable time saved and fewer manual steps per task.

# Why agents?

Single LLM prompts are brittle for real workflows because they cannot reliably:

1. Maintain session state across time.


2. Orchestrate multiple tools with recovery and verification.


3. Split responsibilities across specialty modules.



Agents are the right solution because they:

1. Allow a Planner agent to decompose intent into sub-tasks.


2. Let specialized sub-agents handle search, writing, scheduling, and storage.


3. Enable A2A coordination, loop supervision, and long-running operations with pause/resume.


4. Provide clear traceability and observability for judges.


# TaskSense — Context-Aware Multi-Agent Workflow Manager

## What is TaskSense?
TaskSense is a multi-agent personal assistant that preserves context across sessions, coordinates specialized sub-agents to research, write, and schedule, and stages or executes actions with verifier checks. It is designed for reproducibility in Kaggle and for judges to run without API keys.

## Features demonstrated
- Multi-agent architecture: Planner, Supervisor, Research, Writer, Scheduler.
- Tools: Google Custom Search (simulated by default), Gmail draft, Calendar create (stubs included).
- MCP-style tool adapters and custom NoteStoreTool.
- Sessions & Memory: InMemorySessionService and FAISS-based MemoryBank.
- Long-running operations: pause/resume via Supervisor loop.
- Observability: JSONL logging, tracing and metrics.
- Agent evaluation harness: 10 tasks and metrics for success, recovery, tool precision.

# What I created 

User -> Frontend / Notebook (Kaggle demo) -> TaskSense Orchestrator (Agent Engine pattern)
   
 Planner Agent (Gemini) -> produces plan [steps]
    Supervisor Agent (Loop agent) -> retries, metrics, trace IDs
  Sub-Agents:
        Research Agent -> Google Search tool or Custom Search via MCP
        
Writer Agent -> Gemini-powered rewrite/generate (Gemini sub-agent)
Scheduler Agent -> Calendar API via MCP
Store Agent -> NoteStoreTool (file or DB)
    Memory:
        SessionService (InMemorySessionService) + MemoryBank (FAISS)
    Observability:
        Logging.jsonl, Tracing IDs, Metrics summary
    Verifier:
        Gemini verifier pass per action: APPROVE / REQUIRE_EDIT / DENY

Key requirements satisfied: multi-agent system, MCP/custom tools, long-running ops (pause/resume), sessions & memory, context engineering, observability, agent evaluation, A2A protocol.

# Demo 
We include a Kaggle notebook and simple CLI demo. Example run (simulation mode so judges can run with no keys):

# Input:

User: Update yesterday's research summary on 'Q3 pricing trends', add two bullet points from recent news, and schedule a 20-minute follow-up next week.

# Agent run (what we will show in the notebook):

1. Planner Agent outputs plan:

fetch:previous-summary

research:web:Q3 pricing trends

summarize:merge-update

create:gmail:draft

schedule:calendar:20min



2. Research Agent returns top-3 snippets (simulated or real search results).


3. Writer Agent rewrites merged summary and generates email body.


4. Verifier checks each action; human approval required for actual send/create.


5. Scheduler creates draft calendar event and returns event id.


6. Notebook prints logs, raw outputs, full email draft, and calendar draft JSON.



# We include real sample outputs in the notebook so judges see real evidence:

email_draft.md (full text)

summary.txt (merged summary)

calendar_event.json (title, start, end, description)

logs.jsonl (every step with timestamps and verifier decisions)

metrics.json (success rate, retries)


## How to run (quick)
1. Clone repo

git clone https://github.com/devxtreme001/tasksense.git cd tasksense

2. Create virtualenv and install

python -m venv venv source venv/bin/activate pip install -r requirements.txt

3. Run demo in simulation mode (no API keys required)

python demo/run_demo.py --mode simulation

4. To wire real APIs: set USE_SIMULATION=False in config or set env var TASKSENSE_MODE=real. See `docs/REAL_SETUP.md` for instructions to set up Vertex AI, Custom Search, Gmail, and Calendar.

## Repo structure
See folder tree in this README or run `tree -L 2`.

## Evaluation
Run `python evaluate/harness.py` to run predefined scenario suite. Results will be in `out/metrics.json` and logs in `out/logs.jsonl`.

## Video
A 3-minute pitch script is in `docs/video_script.md`.

## Notes
- Never commit API keys. Use environment variables or GitHub Secrets.
- Default simulation mode ensures reproducibility for judges.
