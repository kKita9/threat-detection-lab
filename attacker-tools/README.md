
# attacker-tools

This module provides scripts and configurations to simulate cyberattacks in a lab environment, primarily for testing SIEM systems.

##  Included Components

- `Dockerfile` – Builds the attacker container based on Kali Linux. It includes several preinstalled tools used for attacks.
- `runner.py` – Randomized attack runner with CLI options
- `attack_launcher.py` – Executes attacks based on a schedule
- `attacks.yaml` – Predefined list of attack scenarios
- `schedule.yaml` – Scheduled execution timeline
- `wordlists/` – Wordlists used for brute-force attacks

##  How to Use

###  Build and start the attacker container (from project root)

```
docker compose up --build -d
```

This container is based on Kali Linux and contains the required attack tools (nmap, sqlmap, hydra, hping3, curl), but the Python scripts are executed locally from the host.

### Run the random attack runner (locally)

```
python attacker-tools/runner.py --mode test --count 3
```

### Run the scheduled attack launcher (locally)

```
python attacker-tools/attack_launcher.py
```

## Tools Used in container

- **nmap** – port scanning
- **sqlmap** – SQL injection testing
- **hydra** – brute-force login attempts
- **hping3** – basic DoS traffic generation
- **curl** – custom HTTP requests

All tools are preinstalled in the container via Kali Linux.

## Logs

All logs are stored in the `logs/attacks/` directory (relative to the project root).

- `attack_runner_details.jsonl` – structured JSONL output for each executed attack
- `attack_runner.log` – log messages from the `runner.py` script
- `attack.log` –  logs from `attack_launcher.py`

## Disclaimer

This setup is intended for testing in **controlled lab environments only**. Do not use it on live networks or external systems!
