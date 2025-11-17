class Supervisor:
    def __init__(self, logger):
        self.logger = logger
    def execute(self, plan, user_request, ts):
        results = {"request": user_request, "plan": plan, "actions": []}
        for step in plan:
            # very simple dispatcher
            if step.startswith("fetch"):
                out = ts.memory.fetch(user_request)  # stub
                results['actions'].append({"step": step, "result": out})
            elif step.startswith("research"):
                out = ts.research_agent.research(user_request)
                results['actions'].append({"step": step, "result": out})
            elif step.startswith("summarize"):
                out = ts.writer_agent.merge_and_summarize(user_request, results)
                results['actions'].append({"step": step, "result": out})
            elif "gmail" in step:
                draft = ts.writer_agent.create_email_draft(user_request)
                results['actions'].append({"step": step, "result": draft})
            elif "schedule" in step:
                ev = ts.scheduler_agent.create_event(user_request)
                results['actions'].append({"step": step, "result": ev})
        results['status'] = 'completed'
        return results
