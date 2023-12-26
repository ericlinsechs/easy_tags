#!/bin/bash

# Specify the package name
PACKAGE_NAME="tag"

# Check if Homebrew is installed
if ! command -v brew >/dev/null 2>&1; then
    echo "Homebrew is not installed. Please install Homebrew from https://brew.sh/."
    exit 1
fi

# Check if the package is installed
if ! brew list "$PACKAGE_NAME" &>/dev/null; then
    echo "$PACKAGE_NAME is not installed. Install $PACKAGE_NAME now."
    brew install "$PACKAGE_NAME"
fi

# Set the path to your virtual environment
VENV_PATH="./venv"

# Activate the virtual environment
source "${VENV_PATH}/bin/activate"

# Now you can run your Python script or commands
python ./app.py