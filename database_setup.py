import subprocess
from pathlib import Path

csv_cleanup_path = Path.cwd() / "data_setup_files" /"data_preprocessing.py"
db_creation_script_path = Path.cwd() / "data_setup_files" /"sqliteDBsetup.py"
num_data_cleanup_script_path = Path.cwd() / "data_setup_files" /"numerical_data_cleanup.py"

subprocess.run(["python",csv_cleanup_path])
subprocess.run(["python",db_creation_script_path])
subprocess.run(["python",num_data_cleanup_script_path ])