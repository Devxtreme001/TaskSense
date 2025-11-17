from ..config import USE_SIMULATION
def simulated_search(q):
    return [{"title": "Fake article A", "snippet": "prices up 5%"}, {"title": "Fake B", "snippet": "supply risk"}]

class SearchTool:
    def run(self, q):
        if USE_SIMULATION:
            return simulated_search(q)
        else:
            raise NotImplementedError("Wire Google Custom Search API here")
