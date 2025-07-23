import argparse
import random
import subprocess
import time
from datetime import datetime
import yaml
import shlex
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "common")))
from logger_utils import setup_logger, jsonl_result

ATACKER_CONTAINER_NAME = 'threat-detection-lab-attacker'
SUCCED_ATTACK_FILE = 'succed_attacks.jsonl'
FAILED_ATTACK_FILE = 'failed_attacks.jsonl'

logger = setup_logger('attack_runner', 'attacks', 'attack_runner.log')

def load_attacks(yaml_path):
    try:
        with open(yaml_path, 'r') as f:
            data = yaml.safe_load(f)
        return data.get('attacks', [])
    except Exception as e:
        logger.error(f"Failed to load YAML file: {e}")
        return []

def filter_attacks(attacks, category=None, intensity=None):
    if category:
        attacks = [a for a in attacks if a['category'] == category]
    if intensity:
        attacks = [a for a in attacks if a['intensity'] == intensity]
    return attacks

def run_attack(attack):
    logger.info(f"Executing attack: {attack['name']}")
    full_command = ['docker', 'exec', ATACKER_CONTAINER_NAME] + shlex.split(attack['command'])
    logger.debug(f'Executing command: {full_command}')
    try:
        result = subprocess.run(full_command, shell=True, capture_output=True, timeout=300)
        success = result.returncode == 0
    except Exception as e:
        result = None
        success = False
        logger.error(f"Execution failed: {e}")
        stderr = str(e)
    else:
        stderr = result.stderr.decode('utf-8', errors='ignore') if result else ''
    
    return {
        'timestamp': datetime.now().isoformat(),
        'attack': attack['name'],
        'category': attack['category'],
        'intensity': attack['intensity'],
        'command': full_command,
        'success': success,
        'exit_code': result.returncode if result else None,
        'stdout': result.stdout.decode('utf-8', errors='ignore') if result else '',
        'stderr': stderr
    }

def main():
    parser = argparse.ArgumentParser(description="SIEM Attack Simulation Runner")
    parser.add_argument('--mode', choices=['continuous', 'test', 'filtered'], default='test')
    parser.add_argument('--count', type=int, default=1)
    parser.add_argument('--category', type=str, help='Filter by category (e.g. brute_force, sql_injection)')
    parser.add_argument('--intensity', type=str, help='Filter by intensity (low, medium, high)')
    parser.add_argument('--min-interval', type=int, default=60)
    parser.add_argument('--max-interval', type=int, default=300)
    parser.add_argument('--yaml', type=str, default='attacks.yaml')
    args = parser.parse_args()

    logger.info('Start attacks ...')

    attacks = load_attacks(args.yaml)
    if not attacks:
        logger.error("No attacks found in the YAML file.")
        return

    attacks = filter_attacks(attacks, args.category, args.intensity)
    if not attacks:
        logger.warning("No attacks matched the filters.")
        return

    if args.mode in ['test', 'filtered']:
        for _ in range(args.count):
            attack = random.choice(attacks)
            result = run_attack(attack)
            log_file = SUCCED_ATTACK_FILE if result['success'] else FAILED_ATTACK_FILE
            jsonl_result(result, 'attacks', log_file)
    elif args.mode == 'continuous':
        while True:
            attack = random.choice(attacks)
            result = run_attack(attack)
            log_file = SUCCED_ATTACK_FILE if result['success'] else FAILED_ATTACK_FILE
            jsonl_result(result, 'attacks', log_file)
            wait_time = random.randint(args.min_interval, args.max_interval)
            logger.info(f"Waiting {wait_time} seconds before the next attack...")
            time.sleep(wait_time)

if __name__ == '__main__':
    main()
