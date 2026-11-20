#!/usr/bin/bash
set -euo pipefail

DATA_DIRS=(
    "data/template"
    "data/resume"
    "data/raw"
    "data/processed"
    "data/plots"
    "data/test"
)
VENV_DIR=".venv"
PYTHON_BIN="${PYTHON_BIN:-python3}"
REQUIREMENTS_FILE="config/requirements.txt"

# Create data directories
echo "Creating data directories..."
for dir in "${DATA_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        mkdir -p "$dir"
        echo "[created] $dir"
    else
        echo "[exists] $dir"
    fi
done

# Create virtual environment
echo "Creating python venv..."
if ! command -v "$PYTHON_BIN" &> /dev/null; then
    echo "Python binary not found: $PYTHON_BIN"
    exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
    "$PYTHON_BIN" -m venv "$VENV_DIR"
    echo "[created] $VENV_DIR"
else
    echo "[exists] $VENV_DIR"
fi

# Install dependencies
if [ -f "$REQUIREMENTS_FILE" ]; then
    echo "Installing dependencies from $REQUIREMENTS_FILE..."
    source "$VENV_DIR/bin/activate"
    pip install --upgrade pip
    pip install -r "$REQUIREMENTS_FILE"
    deactivate
else
    echo "$REQUIREMENTS_FILE not found. Skipping dependency installation."
fi

echo
echo "Setup complete. Next step, run:"
echo "source $VENV_DIR/bin/activate"
