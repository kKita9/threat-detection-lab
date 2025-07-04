
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

This container is based on Kali Linux and contains the attack tools:

- **nmap** – port scanning
- **sqlmap** – SQL injection testing
- **hydra** – brute-force login attempts
- **hping3** – basic DoS traffic generation
- **curl** – custom HTTP requests

You can also manually execute individual attacks by entering the container and running commands directly. For example:
```
docker exec -it attacker bash
```
Run attack: 
```
nmap -sS 172.20.0.10
```

The attacks.yaml file contains a list of predefined attack commands and arguments that can be used as reference or executed manually.


Below are Python scripts that allow you to launch attacks either randomly or on a defined schedule.
Note: Python scripts should be executed from the host machine, not inside the container.

### Run the random attack runner (locally)

```
python attacker-tools/runner.py --mode test --count 3
```

You can customize the behavior of the random attack runner using the following parameters:

--mode – Defines the runner mode. Options:
  - test – randomly selects a given number of attacks without delay
  - continuous – executes attacks with random delays between each attack
  - filtered – allows filtering attacks by category and/or intensity

--count – Number of random attacks to execute (used with test or filtered mode)

--category – Filter attacks by category (e.g. brute_force, sql_injection) - check attack.yaml to more categories

--intensity – Filter attacks by intensity (low, medium, high)

--min-interval – Minimum wait time (in seconds) between attacks (used with continuous mode)

--max-interval – Maximum wait time (in seconds) between attacks (used with continuous mode)

--logfile – Name of the JSONL output file (default: attack_runner_details.jsonl)

--yaml – Path to the YAML file defining the attacks (default: attacks.yaml)


### Run the scheduled attack launcher (locally)

```
python attacker-tools/attack_launcher.py
```


## Logs

All logs are stored in the `logs/attacks/` directory (relative to the project root).

- `attack_runner_details.jsonl` – structured JSONL output for each executed attack
- `attack_runner.log` – log messages from the `runner.py` script
- `attack.log` –  logs from `attack_launcher.py`

## Disclaimer

This setup is intended for testing in **controlled lab environments only**. Do not use it on live networks or external systems!
