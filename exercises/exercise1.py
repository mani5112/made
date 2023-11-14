import pandas as pd
from sqlalchemy import create_engine, Integer, String, Text, Float, DECIMAL

# data url
data_url = "https://opendata.rhein-kreis-neuss.de/api/v2/catalog/datasets/rhein-kreis-neuss-flughafen-weltweit/exports/csv"
#read data and it's delimeted by semi colon
data = pd.read_csv(data_url, delimiter=";")

# Assigning the Datatypes to respective columns
column_types = {
    "column_1": Integer,
    "column_2": Text,
    "column_3": Text,
    "column_4": Text,
    "column_5": String,
    "column_6": String,
    "column_7": Float,
    "column_8": Float,
    "column_9": Integer,
    "column_10": Float,
    "column_11": String,
    "column_12": Text,
    "geo_punkt": DECIMAL,
}

# create SQLite Engine
engine = create_engine("sqlite:///airports.sqlite")

# push the data into SQLite with the table 'airports'
data.to_sql("airports", engine, if_exists="replace", index=False)
