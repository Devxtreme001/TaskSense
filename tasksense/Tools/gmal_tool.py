class GmailTool:
    def create_draft(self, subject, body, to=[]):
        # simulated return
        return {"id": "draft-"+subject[:8], "subject": subject, "body": body, "to": to}
