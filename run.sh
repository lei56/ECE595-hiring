#!/usr/bin/bash
set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"
CONFIG_FILE="config/config.json"
TEST_CONFIG="config/test.json"

# Check input flags
test=false
while getopts "t" opt; do
    case "$opt" in
        t) test=true;;
        *) echo "Usage: $0 [-t]" >&2; exit 1;;
    esac
done

shift $((OPTIND - 1))

# Download templates → /data/template

# Populate templates → /data/resume

# Run experiments, raw results → /data/raw, processed results → /data/processed
if [[ "$test" == true ]]; then
    echo "Running wrapper in test mode with $TEST_CONFIG..."
    "$PYTHON_BIN" src/llm_wrapper.py --config "$TEST_CONFIG"
else
    echo "Running wrapper with config $CONFIG_FILE..."
    "$PYTHON_BIN" src/llm_wrapper.py --config "$CONFIG_FILE"
fi

# Generate plots → /data/plots