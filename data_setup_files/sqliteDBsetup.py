#IMPORTS
import pandas as pd 
import sqlite3
from pathlib import Path


#FUNCTIONS
def load_to_db(file_path:Path, name:str, conn: sqlite3.Connection,excel:bool=False):
    if file_path.exists():
        if excel:
            df = pd.read_excel(file_path)
        else:
            df = pd.read_csv(file_path)
        df.to_sql(name, conn, if_exists='replace', index = False)
        print(f"loaded {name} into database")
    else:
        raise FileNotFoundError(f"Error: {file_path} not found")


# Set the file paths
project_folder = Path.cwd().parent
linkedindata_path = project_folder / "linkedindata"


#create or open linkedindatabase.db, connect to it and create a cursor object
database_file_path = project_folder / "database" / "linkedindatabase.db"
conn = sqlite3.connect(database_file_path)
cur = conn.cursor()
print("Opened database successfully")


#load postings into the database
combined_postings_path = linkedindata_path / "combined_postings.xlsx"
if combined_postings_path.exists():
    load_to_db(combined_postings_path, 'postings',conn,excel=True)
else:
    load_to_db(linkedindata_path / "postings.csv", 'postings',conn)
conn.commit()
print("postings data inserted successfully")


#load tables from folder 'companies' into the database
companies_path = linkedindata_path / "companies"

load_to_db(companies_path / "companies.csv", 'companies',conn)
load_to_db(companies_path / "company_industries.csv", 'company_industries',conn)
load_to_db(companies_path / "company_specialities.csv", 'company_specialities',conn)
load_to_db(companies_path / "employee_counts.csv", 'employee_counts',conn)

conn.commit()
print("companies data inserted successfully")


#loads tables from folder 'jobs' into the database
jobs_path = linkedindata_path / "jobs"

load_to_db(jobs_path / "benefits.csv", 'benefits',conn)
load_to_db(jobs_path / "job_industries.csv", 'job_industries',conn)
load_to_db(jobs_path / "job_skills.csv", 'job_skills',conn)
load_to_db(jobs_path / "salaries.csv", 'salaries',conn)

conn.commit()
print("jobs data inserted successfully")


#loads tables from folder 'mappings' into the database
mappings_path = linkedindata_path / "mappings"

load_to_db(mappings_path / "industries.csv", 'industries',conn)
load_to_db(mappings_path / "skills.csv", 'skills',conn)

conn.commit()
print("mappings data inserted successfully")

#closes cursor and connection
cur.close()
conn.close()
print("Connection closed")