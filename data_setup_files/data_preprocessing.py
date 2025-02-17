# IMPORTS
import pandas as pd 
import numpy as np
import re
import json
from pathlib import Path


# Load parent directory config
config_path_v1= Path.cwd().parent / "local_setup_config.json"
config_path_v2 = Path.cwd() / "local_setup_config.json"
if config_path_v1.exists():
    config_path = config_path_v1
elif config_path_v2.exists():
    config_path = config_path_v2
else:
    raise FileNotFoundError(f"Error: local_setup_config.json not found in project directory")


# Load local config file
if config_path.exists():
    with open(config_path, "r", encoding="utf-8") as file:
        local_config  = json.load(file)
    print('Local configuration file loaded succesfully')
else:
    raise FileNotFoundError(f"Error: {config_path} not found")

# Set parent folder
project_folder = Path(local_config["parent_folder"]).resolve()
#print(f"Project folder set to {project_folder} for data_preprocessing.py")

# Set the file paths
project_folder = Path.cwd()
print(f"Project folder set to {project_folder} for data_preprocessing.py")
output_path = project_folder / "linkedindata"
postings_file_path = output_path / "postings.csv"
combined_file_path = output_path / "combined_postings.xlsx"

# Function to clean invalid characters
def remove_illegal_chars(value):
    if isinstance(value, str):  # Apply only to text fields
        return re.sub(r"[\x00-\x1F\x7F]", "", value)  # Remove ASCII control characters
    return value

try:
    df = pd.read_csv(postings_file_path)

    # Clean invalid characters in all data
    df = df.map(remove_illegal_chars)

    # Calculate the number of rows in each chunk
    num_rows = len(df)
    chunk_size = num_rows // 4  # Split into 4 equal parts

    # Split the data into 4 parts and save each as a separate Excel file
    for i in range(4):
        start_row = i * chunk_size
        end_row = (i + 1) * chunk_size if i < 3 else num_rows  # Include all remaining rows in the last part

        chunk = df.iloc[start_row:end_row]
        part = f"postings_part_{i + 1}.xlsx"
        output_file = output_path / part
        output_file_str = str(output_file)
        chunk.to_excel(output_file, index=False)

        print(f"Part {i + 1} saved as {output_file_str}.")

except Exception as e:
    print("An error occurred. Error details are below:")
    import traceback
    traceback.print_exc()


#RECONSTRUCT INITIAL POSTINGS FILE
# File paths for the parts
file_paths = [
    output_path / "postings_part_1.xlsx",
    output_path / "postings_part_2.xlsx",
    output_path / "postings_part_3.xlsx",
    output_path / "postings_part_4.xlsx"
]

# Combine all parts into a single DataFrame
combined_df = pd.concat([pd.read_excel(fp) for fp in file_paths], ignore_index=True)

# Save the combined file as a new Excel file
combined_file_path = output_path / "combined_postings.xlsx"
combined_df.to_excel(combined_file_path, index=False)

print(f"Combined file has been saved as {output_file}.")

#Delete all parts
n=1
for fp in file_paths:
    if fp.exists():
        fp.unlink()
        print(f"deleted temporal 'postings' partition {n}")
    n+=1


