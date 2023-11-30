#!/bin/bash

# Check if URL is provided as an argument
if [ $# -eq 0 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sI "$1" | grep -i Content-Length | awk '{print $2}' | cut -c1-10
