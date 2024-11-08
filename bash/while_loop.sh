#!/bin/bash

counter=0

while [ $counter -lt 5 ]; do
    echo "Looping..."
    sleep 2
    echo "$counter is less than 5"
    
    # Incrementing counter
    counter=$(( counter + 1 ))

    echo
done

echo "Out of the loop..."
