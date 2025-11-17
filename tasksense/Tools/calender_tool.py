class CalendarTool:
    def create_event(self, title, start, end, description):
        return {"id": "evt-"+title[:6], "title": title, "start": start, "end": end, "description": description}
