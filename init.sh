#!/bin/bash


echo "Initializing log directories and files..."

mkdir -p ./logs/ssh-lab

# Tworzymy pliki logów, które będą używane przez rsyslog
touch ./logs/ssh-lab/auth.log
touch ./logs/ssh-lab/syslog
touch ./logs/ssh-lab/secure
touch ./logs/ssh-lab/messages

# Ustawiamy odpowiednie uprawnienia
chmod 666 ./logs/ssh-lab/*.log

echo "Done. You can now run: docker compose up --build -d"
