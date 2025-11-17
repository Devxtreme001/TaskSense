class WriterAgent:
    def __init__(self, logger):
        self.logger = logger
    def merge_and_summarize(self, request, results):
        # naive merge simulation
        summary = "Merged summary: prices rose 5%, supply consolidation, prepare slides."
        return summary
    def create_email_draft(self, request):
        subj = "Follow-up: " + request[:40]
        body = "Team, here is the summary and next steps..."
        return {"subject": subj, "body": body}
