# SSH Lab

This container provides a basic SSH server for simulating brute-force attacks and testing detection techniques.

## Features

- Based on Ubuntu 22.04
- Root login enabled
- Password authentication enabled
- Verbose SSH logging (LogLevel VERBOSE)
- System logs stored in /var/log/auth.log and /var/log/syslog
- Integrated with rsyslog

## Default credentials

- Username: root
- Password: root123

## Usage

This container is built and launched via Docker Compose from the main project:

    docker-compose up -d ssh-lab

SSH will be exposed on port 2222 of the host:

    ssh root@127.0.0.1 -p 2222

## Logs

Log files from the container are persisted to the host under:

    ./logs/ssh-lab/auth.log
    ./logs/ssh-lab/syslog
