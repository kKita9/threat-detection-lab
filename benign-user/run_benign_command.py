import yaml
import time
import subprocess
from datetime import datetime
from pathlib import Path

activity_files = [
    "/app/activities/ssh_activity.yaml",
    "/app/activities/ftp_activity.yaml",
    "/app/activities/dvwa_activity.yaml"
]

log_dir = Path("/app/logs")
log_dir.mkdir(parents=True, exist_ok=True)
log_file = log_dir / "benign_command_log.txt"

def load_all_commands():
    commands = []
    for file_path in activity_files:
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
            for entry in data:
                commands.append({
                    "name": entry.get("name", "Unnamed"),
                    "command": entry.get("command", ""),
                    "target": entry.get("target", "unknown"),
                    "user": entry.get("user", "unknown"),
                    "source_file": Path(file_path).name
                })
    return commands

def log_entry(entry):
    with open(log_file, "a") as f:
        f.write(entry + "\n")

def run_commands_with_interval(commands, interval_seconds=180):
    for idx, cmd in enumerate(commands, start=1):
        start_time = datetime.now()
        log_entry(f"[{start_time.strftime('%Y-%m-%d %H:%M:%S')}] START #{idx}: {cmd['name']} (from {cmd['source_file']})")
        log_entry(f"  Command: {cmd['command']}")

        try:
            result = subprocess.run(cmd["command"], shell=True, capture_output=True, text=True, timeout=60)
            log_entry(f"  Output: {result.stdout.strip()}")
            log_entry(f"  Error: {result.stderr.strip()}")
        except subprocess.TimeoutExpired:
            log_entry("  ERROR: Command timed out after 60 seconds.")

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        log_entry(f"[{end_time.strftime('%Y-%m-%d %H:%M:%S')}] END #{idx}: Duration: {duration:.1f}s\n")

        if idx < len(commands):
            time.sleep(interval_seconds)

if __name__ == "__main__":
    all_cmds = load_all_commands()
    run_commands_with_interval(all_cmds, interval_seconds=180)
