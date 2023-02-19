import argparse
import logging
import subprocess

# Set up command line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("python_file", help="The Python file to execute")
parser.add_argument("log_file", help="The destination for the log file")
parser.add_argument("logging_type", choices=["debug", "info", "warning", "error", "critical"], help="The type of logging to use")
args = parser.parse_args()

# Set up logging
logging.basicConfig(filename=args.log_file, level=getattr(logging, args.logging_type.upper()))

# Execute the specified Python file
try:
    result = subprocess.run(["python", args.python_file], capture_output=True, text=True)
    logging.info(f"Script execution succeeded with output:\n{result.stdout}")
except subprocess.CalledProcessError as e:
    logging.error(f"Script execution failed with error:\n{e.stderr}")
