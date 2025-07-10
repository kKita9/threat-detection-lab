#!/bin/bash

echo "Initializing log directories and files..."

LOG_ROOT="$(dirname "$0")/../logs"
mkdir -p "$LOG_ROOT"

# SSH-lab logs
mkdir -p "$LOG_ROOT/ssh-lab"
touch "$LOG_ROOT/ssh-lab/auth.log"
chmod 666 "$LOG_ROOT/ssh-lab/auth.log"

# FTP-lab logs
mkdir -p "$LOG_ROOT/ftp-lab"
touch "$LOG_ROOT/ftp-lab/vsftpd.log"
chmod 666 "$LOG_ROOT/ftp-lab/vsftpd.log"

# DVWA logs
mkdir -p "$LOG_ROOT/dvwa/apache2"
mkdir -p "$LOG_ROOT/dvwa/mysql"
touch "$LOG_ROOT/dvwa/apache2/access.log"
touch "$LOG_ROOT/dvwa/apache2/error.log"
touch "$LOG_ROOT/dvwa/mysql/error.log"
chmod 666 "$LOG_ROOT/dvwa/apache2/"*.log
chmod 666 "$LOG_ROOT/dvwa/mysql/"*.log

# Suricata logs
mkdir -p "$LOG_ROOT/suricata/ssh"
mkdir -p "$LOG_ROOT/suricata/ftp"
mkdir -p "$LOG_ROOT/suricata/dvwa"

# Attacker logs
mkdir -p "$LOG_ROOT/attacks"

# Benign user logs
mkdir -p "$LOG_ROOT/benign"

echo "Done. You can now run: docker compose up --build -d"
