# PyScriptLogger

# Summary

A script that acts as a command line tool to pass Python scripts to so that logging of the scripts performance can be monitored on several levels including: "debug", "info", "warning", "error" or "critical"

You can then run this script from the command line by specifying the python file, log file, and logging type like so:
python my_script.py my_python_file.py my_log_file.log debug

And the script will execute the specified python file, log the output to the specified log file using the specified logging type.

----------------------------------------------------------------------------------------------------------------------------------------------------

# Formal Documentation

This script executes a specified Python file and logs the results to a specified file using the specified logging type. The script accepts three command line arguments:

python_file: The path to the Python file to execute
log_file: The path to the file to save the log output
logging_type: The type of logging to use, which can be one of the following options: "debug", "info", "warning", "error", or "critical".

# Usage
python execute_and_log.py python_file log_file logging_type


# Arguments
python_file: The path to the Python file to execute
log_file: The path to the file to save the log output
logging_type: The type of logging to use, which can be one of the following options: "debug", "info", "warning", "error", or "critical".

# Dependencies
This script requires the following packages to be installed:

argparse
logging
subprocess

# Functionality
This script performs the following steps:

Parses the command line arguments using the argparse package.
Sets up the logging using the specified logging type and saves the output to the specified log file using the logging package.
Executes the specified Python file using the subprocess package and captures the output.
Logs the output of the script execution to the log file using the logging package. If the execution fails, it logs the error message to the log file.
