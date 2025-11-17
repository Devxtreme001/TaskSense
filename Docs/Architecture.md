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
