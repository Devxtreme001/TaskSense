from tasksense.agent import TaskSense
from tasksense.config import USE_SIMULATION
import json
ts = TaskSense()
task = "Update yesterday's research summary on Q3 pricing trends, add two news bullets, schedule 20-min follow-up next week."
out = ts.run(task)
print(json.dumps(out, indent=2))
