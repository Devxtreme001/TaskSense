from .config import USE_SIMULATION
def call_model(prompt):
    # simulation. Replace with Vertex AI call
    if USE_SIMULATION:
        if "plan" in prompt.lower():
            return ["fetch:previous-summary", "research:web", "summarize:merge", "create:gmail_draft", "schedule:calendar"]
        return "Simulated model output"
    else:
        raise NotImplementedError("Wire Vertex AI call here")

class Planner:
    def plan(self, user_request: str):
        prompt = f"Plan steps for: {user_request}"
        steps = call_model(prompt)
        return steps
