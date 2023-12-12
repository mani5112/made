import pandas as pd
import sqlite3

url = "https://www-genesis.destatis.de/genesis/downloads/00/tables/46251-0021_00.csv"
# ignoring the first 6 lines(rows) and last 4 lines(skip footer)
df = pd.read_csv(url, sep=";", encoding='ISO-8859-1', skiprows=6, skipfooter=4, engine='python')


# keeping only the following names
columns_to_keep = ['Unnamed: 0', 'Unnamed: 1', 'Unnamed: 2', 'Insgesamt', 'Insgesamt.1', 'Insgesamt.2', 'Insgesamt.3', 'Insgesamt.4', 'Insgesamt.5', 'Insgesamt.6']
# renmae_column names
new_column_names = ['date', 'CIN', 'name', 'petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']

column_mapping = dict(zip(columns_to_keep, new_column_names))
# renaming the column names
df.rename(columns=column_mapping, inplace=True)
# new df
df = df[new_column_names]

#validating data
# Validate CINs
df['CIN'] = df['CIN'].astype(str).str.zfill(5)

# Validate positive integers >0
numeric_columns = ['petrol', 'diesel', 'gas', 'electro', 'hybrid', 'plugInHybrid', 'others']
df = df.loc[(df[numeric_columns].apply(pd.to_numeric, errors='coerce') > 0).all(axis=1)]

print(df)

# Using fitting SQLite types
# Define SQLite types
sqlite_types = {'date': 'TEXT', 'CIN': 'TEXT', 'name': 'TEXT',
                'petrol': 'INTEGER', 'diesel': 'INTEGER', 'gas': 'INTEGER',
                'electro': 'INTEGER', 'hybrid': 'INTEGER', 'plugInHybrid': 'INTEGER', 'others': 'INTEGER'}

# Write data to SQLite database
conn = sqlite3.connect('cars.sqlite')
df.to_sql('cars', conn, index=False, if_exists='replace', dtype=sqlite_types)
conn.close()
