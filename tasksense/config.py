import os
USE_SIMULATION = os.getenv("TASKSENSE_MODE", "simulation") == "simulation"
LOG_PATH = os.getenv("TASKSENSE_LOG", "out/logs.jsonl")
METRICS_PATH = os.getenv("TASKSENSE_METRICS", "out/metrics.json")
