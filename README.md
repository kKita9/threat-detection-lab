# Threat Detection Lab

This project provides a small and practical environment for testing and analyzing various cyberattacks using different threat detection methods. It includes a lab setup with vulnerable services and logs exposed for further analysis by a detection engine (SIEM or custom tools).

## Lab Environments

The following vulnerable services are included under the environments/ directory:

- **SSH-Lab**: Custom-built container with OpenSSH server and verbose logging enabled.
- **FTP-Lab**: Custom-built container with vsFTPd server and full logging support.
- **DVWA**: Dockerized version of Damn Vulnerable Web Application for simulating SQL injection, XSS, and other web attacks.

### Support Tools
- **Attacker Tools** – Python scripts and a Kali Linux-based container for launching simulated attacks (e.g. brute-force, SQL injection, port scanning) against the lab services. Useful for testing detection methods and generating labeled log data.

## Folder Structure

```
threat-detection-lab/
├── environments/
│   ├── ssh-lab/
│   ├── ftp-lab/
│   ├── dvwa/
├── attacker-tools/
├── common/
├── logs/
│   ├── ssh-lab/
│   ├── ftp-lab/
│   ├── dvwa/
│   ├── attacks/
├── init.sh
├── docker-compose.yml
```

## Getting Started

1. Clone this repository
2. Initialize required folders and files:
   ```bash
   ./init.sh
   ```
3. Build and start the containers:
   ```bash
   docker compose up --build -d
   ```

## Exposed Ports

- **SSH-Lab**: localhost:2222
- **FTP-Lab**: localhost:2121
- **DVWA**: localhost:8080

## Logging

Each service logs authentication attempts and events to host-mounted volumes under the `logs/` directory for easy monitoring and analysis.

## Use Cases

This environment is suitable for:

- Simulating and capturing brute-force, port scan, and injection attacks
- Testing supervised and unsupervised detection algorithms
- Developing or integrating with SIEM solutions
