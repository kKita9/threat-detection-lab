#!/bin/bash

LOG_DIR="$(dirname "$0")/../logs"

if [ -d "$LOG_DIR" ]; then
  echo "Cleaning folder: $LOG_DIR"
  find "$LOG_DIR" -mindepth 1 -exec rm -rf {} +
  echo " Ready."
else
  echo "The $LOG_DIR doesn't exist."
fi
