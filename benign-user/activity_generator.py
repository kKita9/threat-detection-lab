import time
import random
import subprocess
import yaml
import os
import sys
import socket
import glob

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.logger_utils import setup_logger, jsonl_result

MIN_SLEEP = float(os.getenv("MIN_SLEEP", 1))
MAX_SLEEP = float(os.getenv("MAX_SLEEP", 5))
MIN_COMMANDS = int(os.getenv("MIN_COMMANDS", 1))
MAX_COMMANDS = int(os.getenv("MAX_COMMANDS", 5))

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACTIVITY_FOLDER = os.path.join(BASE_DIR, "activities")

logger = setup_logger("benign_runner", "benign", "benign_runner.log")
logger.info(f"Loaded ENV config: MIN_SLEEP={MIN_SLEEP}, MAX_SLEEP={MAX_SLEEP}, MIN_COMMANDS={MIN_COMMANDS}, MAX_COMMANDS={MAX_COMMANDS}")

activity_files = glob.glob(os.path.join(ACTIVITY_FOLDER, "*_activity.yaml"))
commands = []

for filepath in activity_files:
    try:
        with open(filepath, "r") as f:
            entries = yaml.safe_load(f)
            if isinstance(entries, list):
                commands.extend(entries)
            else:
                logger.warning(f"File {filepath} is not a list, skipping.")
    except Exception as e:
        logger.error(f"Failed to load {filepath}: {e}")

if not commands:
    logger.error("No valid commands found in activity files.")
    sys.exit(1)

while True:
    count = random.randint(MIN_COMMANDS, MAX_COMMANDS)
    selected = random.choices(commands, k=count)

    for command_entry in selected:
        command = command_entry.get("command")
        user = command_entry.get("user", "unknown")
        target = command_entry.get("target", "n/a")

        logger.info(f"[{user}] Executing: {command}")
        try:
            start_exec = time.time()
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=15)
            duration = time.time() - start_exec

            output = result.stdout.strip()
            error = result.stderr.strip()

            if result.returncode != 0:
                logger.warning(f"[{user}] Command failed with return code {result.returncode}")

            log_data = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
                "user": user,
                "target": target,
                "command": command,
                "return_code": result.returncode,
                "duration": duration,
                "stdout": output,
                "stderr": error,
            }
            jsonl_result(log_data, "benign", "benign_runner_details.jsonl")

        except Exception as e:
            logger.error(f"[{user}] Error executing command: {e}")

    time.sleep(random.uniform(MIN_SLEEP, MAX_SLEEP))