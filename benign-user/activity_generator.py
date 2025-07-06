import time
import random
import subprocess
import yaml
import os
import sys
import socket
import glob

# Add parent folder to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from common.logger_utils import setup_logger, jsonl_result

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ACTIVITY_FOLDER = os.path.join(BASE_DIR, "activities")

# Setup logger
logger = setup_logger("benign_runner", "benign", "benign_runner.log")

# Active connections tracking
target_status = {}

# Load all YAML activity files
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

# Main execution loop
while True:
    command_entry = random.choice(commands)
    name = command_entry.get("name")
    command = command_entry.get("command")
    target = command_entry.get("target")
    user = command_entry.get("user")
    requires_session = command_entry.get("requires_session", True)
    credentials = command_entry.get("credentials", {})

    # Special case: exit
    if command.strip() == "exit":
        if target in target_status and target_status[target] == user:
            logger.info(f"[{user}] disconnecting from {target}")
            del target_status[target]
        time.sleep(random.uniform(2, 5))
        continue

    # Auto-wrap SSH commands with sshpass if needed
    if command.startswith("ssh ") and "sshpass" not in command:
        password = credentials.get("password", "root123")
        command = f"sshpass -p '{password}' {command}"

    # Session logic
    if command.startswith("ssh") or command.startswith("ftp"):
        if target_status.get(target) == user:
            logger.info(f"[{user}] already connected to {target}, skipping login")
            time.sleep(random.uniform(2, 5))
            continue
        else:
            target_status[target] = user
    elif requires_session:
        if target and target in target_status and target_status[target] != user:
            logger.info(f"[{user}] not logged into {target}, skipping '{command}'")
            time.sleep(random.uniform(2, 5))
            continue

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
            "user": user,
            "target": target,
            "command": command,
            "stdout": output,
            "stderr": error,
            "return_code": result.returncode,
            "duration": duration,
            "timestamp": time.time()
        }
        jsonl_result(log_data, "benign", "benign_runner_details.jsonl")

    except Exception as e:
        logger.error(f"[{user}] Error executing command: {e}")

    time.sleep(random.uniform(3, 10))
