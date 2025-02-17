import sys
import subprocess
from pathlib import Path

csv_cleanup_path = Path.cwd() / "data_setup_files" /"data_preprocessing.py"
db_creation_script_path = Path.cwd() / "data_setup_files" /"sqliteDBsetup.py"
num_data_cleanup_script_path = Path.cwd() / "data_setup_files" /"numerical_data_cleanup.py"

subprocess.run([r".venv\Scripts\python.exe",csv_cleanup_path])
subprocess.run([r".venv\Scripts\python.exe",db_creation_script_path])
subprocess.run([r".venv\Scripts\python.exe",num_data_cleanup_script_path])