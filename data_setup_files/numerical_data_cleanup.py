#run this only after completing sqliteDBsetup.py execution


#IMPORTS
import sqlite3
import pandas as pd
import numpy as np
from pathlib import Path


#SET PROJECT FOLDER MAIN DIRECTORY
project_folder = Path.cwd().parent


#DATABASE CONNECTION
linkedindatabase_path = project_folder / "database" / "linkedindatabase.db"
if linkedindatabase_path.exists():
    conn = sqlite3.connect(linkedindatabase_path)
else:
    raise FileNotFoundError(f"Error: {linkedindatabase_path} not found")


#Create numerical_postings table in database
query = "SELECT job_id, max_salary, pay_period, views, med_salary, min_salary, applies, original_listed_time, expiry, closed_time, listed_time, currency, normalized_salary FROM postings"
df = pd.read_sql(query, conn)
df.head()
df.to_sql('numerical_postings', conn, if_exists='replace', index = False)
conn.commit()


#Salary normalization
df_numerical = pd.read_sql('SELECT * FROM numerical_postings', conn)

#Convert Null in 'currency' to USD
#df_numerical['currency'] = df_numerical['currency'].fillna('USD')

#Convert other currencies to USD
conversion_rates = {'USD': 1, 'EUR': 1.18, 'GBP': 1.38, 'AUD': 0.74, 'CAD': 0.79, 'BBD': 0.50}

df_numerical['max_salary'] = df_numerical.apply(
    lambda x: conversion_rates[x['currency']] * x['max_salary']
    if not pd.isna(x['currency']) and not pd.isna(x['max_salary'])
    else np.nan,
    axis=1
)

df_numerical['max_salary'] = df_numerical.apply(
    lambda x: conversion_rates[x['currency']] * x['max_salary']
    if not pd.isna(x['currency']) and not pd.isna(x['max_salary'])
    else np.nan,
    axis=1
)

df_numerical['min_salary'] = df_numerical.apply(
    lambda x: conversion_rates[x['currency']] * x['min_salary']
    if not pd.isna(x['currency']) and not pd.isna(x['min_salary'])
    else np.nan,
    axis=1
)

df_numerical['med_salary'] = df_numerical.apply(
    lambda x: conversion_rates[x['currency']] * x['med_salary']
    if not pd.isna(x['currency']) and not pd.isna(x['med_salary'])
    else np.nan,
    axis=1
)

df_numerical['normalized_salary'] = df_numerical.apply(
    lambda x: conversion_rates[x['currency']] * x['normalized_salary']
    if not pd.isna(x['currency']) and not pd.isna(x['normalized_salary'])
    else np.nan,
    axis=1
)

#CONVERT PAY PERIOD TO ANNUAL SALARY
time_multiplier = {'HOURLY': 40*52, 'WEEKLY': 52, 'BIWEEKLY': 26, 'MONTHLY': 12, 'YEARLY': 1}

def convert_to_annual_max(row):
    if not pd.isna(row['max_salary']):
        if not pd.isna(row['pay_period']):
            if not (row['pay_period'] == 'HOURLY' and row['max_salary'] > 10000):
                return time_multiplier[row['pay_period']] * row['max_salary']
    return row['max_salary']
    
def convert_to_annual_med(row):
    if not pd.isna(row['med_salary']):
        if not pd.isna(row['pay_period']):
            if not (row['pay_period'] == 'HOURLY' and row['med_salary'] > 10000):
                return time_multiplier[row['pay_period']] * row['med_salary']
    return row['med_salary']

def convert_to_annual_min(row):
    if not pd.isna(row['min_salary']):
        if not pd.isna(row['pay_period']):
            if not (row['pay_period'] == 'HOURLY' and row['min_salary'] > 10000):
                return time_multiplier[row['pay_period']] * row['min_salary']
    return row['min_salary']
    



df_numerical['max_salary'] = df_numerical.apply(
    convert_to_annual_max,
    axis=1
)


df_numerical['min_salary'] = df_numerical.apply(
    convert_to_annual_min,
    axis=1
)

df_numerical['med_salary'] = df_numerical.apply(
    convert_to_annual_med,
    axis=1
)

#Create clean_numerical_postings in database
df_numerical.to_sql('clean_numerical_postings', conn, if_exists='replace', index = False)
conn.commit()

#Close connection
conn.close()