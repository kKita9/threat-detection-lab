#!/bin/bash


echo "Initializing log directories and files..."

mkdir -p ./logs/ssh-lab

# files used by rsyslog rsyslog
touch ./logs/ssh-lab/auth.log
touch ./logs/ssh-lab/syslog
touch ./logs/ssh-lab/secure
touch ./logs/ssh-lab/messages

# ftp logs
mkdir -p logs/ftp-lab
touch logs/ftp-lab/vsftpd.log

chmod 666 ./logs/ssh-lab/*.log

echo "Done. You can now run: docker compose up --build -d"
