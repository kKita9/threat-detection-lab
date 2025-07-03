import yaml
import time
import subprocess
from datetime import datetime
import logging
import os 

log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'attacks')
os.makedirs(log_path, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_path, 'attack.log'),
    level=logging.INFO,
    format='[%(asctime)s] %(message)s'
)

def load_schedule(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def wait_until(start_time_str):
    start_time = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    while datetime.now() < start_time:
        time.sleep(1)

def run_command_in_container(container_name, command):
    full_command = ['docker', 'exec', container_name] + command.split()
    logging.info(f"Launching attack: {' '.join(full_command)}")
    try:
        output = subprocess.check_output(full_command, stderr=subprocess.STDOUT)
        logging.info(output.decode())
    except subprocess.CalledProcessError as e:
        logging.error(e.output.decode())

def main():
    schedule = load_schedule('schedule.yaml')
    for attack in schedule:
        if 'sleep' in attack:
            logging.info(f"Sleeping for {attack['sleep']} seconds before next attack")
            time.sleep(attack['sleep'])
        elif 'start_time' in attack:
            logging.info(f"Waiting until {attack['start_time']}")
            wait_until(attack['start_time'])

        run_command_in_container('attacker', attack['command'])

if __name__ == "__main__":
    main()
