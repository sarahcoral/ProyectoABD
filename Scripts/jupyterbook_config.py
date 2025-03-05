import yaml
from pathlib import Path
import json

given_project_folder = None

#SET PROJECT FOLDER MAIN DIRECTORY
if given_project_folder == None:
    start_path = Path.cwd()

    current_path = start_path
    # If we reached the root without finding the folder, return None
    project_folder = None
    # Traverse up the directory tree
    while current_path != current_path.parent:  # While not at the root directory
        if current_path.name == 'ProyectoABD':
            project_folder = current_path
        current_path = current_path.parent
else:
    project_folder = given_project_folder
print(f"Project folder set to {project_folder} for jupyterbook_config.py")

#LOAD LOCAL_SETUP_CONFIG FILE
config_path = project_folder / "local_setup_config.json"
if config_path.exists():
    with open(config_path, "r", encoding="utf-8") as file:
        local_config  = json.load(file)
else:
    raise FileNotFoundError(f"Error: {config_path} not found")
    
# set run_local
run_local = local_config["run_local"]


# Define local and online TOC configurations
local_toc = {
    'format': 'jb-article',
    'root': 'visualization_notebooks/index',
    'sections': [
        {'file': 'visualization_notebooks/notebooks'},
        {'file': 'visualization_notebooks/markdown-notebooks'},
        {'file': 'visualization_notebooks/index'},
        {'file': 'visualization_notebooks/load_database'},
        {'file': 'visualization_notebooks/summary_data_processing'},
        {'file': 'visualization_notebooks/descriptive_analysis'},
        {'file': 'visualization_notebooks/exploratory_analysis'},
        {'file': 'visualization_notebooks/predictive_analysis'},
        {'file': 'visualization_notebooks/conclusions'},
        {'file': 'visualization_notebooks/bibliography'}
    ]
}

online_toc = {
    'format': 'jb-article',
    'root': 'visualization_notebooks/index',
    'sections': [
        {'file': 'visualization_notebooks/notebooks'},
        {'file': 'visualization_notebooks/markdown-notebooks'},
        {'file': 'visualization_notebooks/index'},
        {'file': 'visualization_notebooks/summary_data_processing'},
        {'file': 'visualization_notebooks/descriptive_analysis_preloaded'},
        {'file': 'visualization_notebooks/exploratory_analysis_preloaded'},
        {'file': 'visualization_notebooks/predictive_analysis_preloaded'},
        {'file': 'visualization_notebooks/conclusions'},
        {'file': 'visualization_notebooks/bibliography'}
    ]
}

# Set the correct TOC based on the environment
if not run_local:
    toc_data = online_toc
else:
    toc_data = local_toc

# Load the current toc.yaml, modify it, and save it back
toc_file = str(project_folder / "proyectoabdbook" / "_toc.yaml")

# Write the correct TOC to toc.yaml
with open(toc_file, 'w') as file:
    yaml.dump(toc_data, file)

environment = 'local'
if not run_local:
    environment = 'remote'

print(f"TOC has been updated for the {environment} environment.")
