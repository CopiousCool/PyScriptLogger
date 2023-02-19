# PyScriptLogger
A script that acts as a command line tool to pass Python scripts to so that logging of the scripts performance can be monitored on several levels including: "debug", "info", "warning", "error" or "critical"

You can then run this script from the command line by specifying the python file, log file, and logging type like so:
python my_script.py my_python_file.py my_log_file.log debug

And the script will execute the specified python file, log the output to the specified log file using the specified logging type.
