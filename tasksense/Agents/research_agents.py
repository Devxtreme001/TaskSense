class ResearchAgent:
    def __init__(self, search_tool, logger):
        self.search_tool = search_tool
        self.logger = logger
    def research(self, query):
        out = self.search_tool.run(query)
        self.logger.log("research", {"query": query, "out": out})
        return out
