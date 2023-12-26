#!/bin/bash

# Specify the package name
PACKAGE_NAME="tag"

# Check if pip is installed
if ! command -v pip >/dev/null 2>&1; then
    echo "pip is not installed. Please install pip."
    exit 1
fi

pip install -r requirements.txt

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

# Now you can run your Python script or commands
python ./app.py