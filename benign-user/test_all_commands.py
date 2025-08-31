import yaml
import subprocess
import os
import glob
from datetime import datetime

ACTIVITY_DIR = "/app/activities"
OUTPUT_FILE = "/app/test_output.log"

def log(msg):
    with open(OUTPUT_FILE, "a") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {msg}\n")

def run_command(name, command):
    log(f"Running: {name}")
    log(f"Command: {command}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=15)
        log(f"Return code: {result.returncode}")
        log(f"STDOUT:\n{result.stdout.strip()}")
        log(f"STDERR:\n{result.stderr.strip()}")
    except Exception as e:
        log(f"Error: {e}")
    log("-" * 80)

def main():
    if not os.path.exists(ACTIVITY_DIR):
        print(f"Activity folder not found: {ACTIVITY_DIR}")
        return

    activity_files = glob.glob(os.path.join(ACTIVITY_DIR, "*_activity.yaml"))
    if not activity_files:
        print("No activity YAML files found.")
        return

    log(f"Starting command test across {len(activity_files)} activity files.\n")

    for file_path in activity_files:
        log(f"--- Executing commands from: {os.path.basename(file_path)} ---")
        try:
            with open(file_path, "r") as f:
                entries = yaml.safe_load(f)
        except yaml.YAMLError as e:
            log(f"Error reading YAML: {e}")
            continue

        if not isinstance(entries, list):
            log(f"Invalid structure in {file_path}")
            continue

        for entry in entries:
            name = entry.get("name", "Unnamed")
            command = entry.get("command", "")
            if command.strip().lower() == "exit":
                log(f"Skipping 'exit' pseudo-command: {name}")
                continue
            run_command(name, command)

    log("All commands processed.\n")

if __name__ == "__main__":
    main()
