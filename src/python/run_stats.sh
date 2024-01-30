#!/bin/bash

# Check if the Python script file is provided as an argument
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <python_script.py>"
    exit 1
fi

# Get the Python script file name from the command line argument
python_script="$1"

# Check if the Python interpreter is available
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is not installed. Please install Python 3."
    exit 1
fi

# Execute the Python script using Python 3
python3 "$python_script"


# Added by Mouli
# ------------------------------------------------
# after saving this file do these from terminal: 
# chmod +x run_stats.sh

# execute the python file by below cmd
# ./run_stats.sh your_python_script.py