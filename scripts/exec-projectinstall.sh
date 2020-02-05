#!/bin/sh

echo "Initial install of the Project"

echo "Running install: 'pip3 install -e .' in the folder with setup.py"
pip3 install -e .
pip3 install -e .[test]

# run cleanup tools
# black __main__.py
# isort __main__.py
# flake8 __main__.py

# echo "Show Packages"
# echo "pip3 show requests"

echo "List Packages"
# pip3 list --format=columns | grep myproject
pip3 list --format=columns

