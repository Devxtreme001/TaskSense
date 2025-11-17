from .planner import Planner
from .verifier import Verifier
from .agents.research_agent import ResearchAgent
from .agents.writer_agent import WriterAgent
from .agents.scheduler_agent import SchedulerAgent
from .tools.search_tool import SearchTool
from .tools.gmail_tool import GmailTool
from .tools.calendar_tool import CalendarTool
from .memory.memory_bank import MemoryBank
from .supervisor import Supervisor
from .observability import Logger
from .config import USE_SIMULATION

class TaskSense:
    def __init__(self):
        self.logger = Logger()
        self.memory = MemoryBank()
        self.search_tool = SearchTool()
        self.gmail_tool = GmailTool()
        self.calendar_tool = CalendarTool()
        self.planner = Planner()
        self.verifier = Verifier()
        self.research_agent = ResearchAgent(self.search_tool, self.logger)
        self.writer_agent = WriterAgent(self.logger)
        self.scheduler_agent = SchedulerAgent(self.calendar_tool, self.logger)
        self.supervisor = Supervisor(self.logger)
    def run(self, user_request: str, require_human_approve: bool = True):
        plan = self.planner.plan(user_request)
        return self.supervisor.execute(plan, user_request, self)
