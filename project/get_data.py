import opendatasets as od
import sqlite3
import pandas as pd
import logging

# dataset links
dataset_links = [
  "https://www.kaggle.com/datasets/kingburrito666/elon-musk-tweets", # elon must tweets
  "https://www.kaggle.com/datasets/timoboz/tesla-stock-data-from-2010-to-2020" # tesla stocks
]

# have to provide kaggle json file to download the .csv files
od.download(dataset_links[0])
od.download(dataset_links[1])

# storing the elon must tweets into a sqlite database
path_elon_tweets = 'elon-musk-tweets/elonmusk_tweets.csv'
df_tweets = pd.read_csv(path_elon_tweets)
tweet_db_path = '../data/elon_tweets.sqlite'
logging.info(f'storing the tweets data into a database under data folder ')
conn = sqlite3.connect(tweet_db_path)
df_tweets.to_sql('elon_tweets', conn, index=False, if_exists='replace')

# storing the tesla tweets into a sqlite dataase
path_tesla_stocks = 'tesla-stock-data-from-2010-to-2020/TSLA.csv'
airbnb_df = pd.read_csv(path_tesla_stocks)
tsla_stock_db_path = '../data/tsla_stocks.sqlite'
conn = sqlite3.connect(tsla_stock_db_path)
logging.info(f'storing the stocks data into a database under data folder ')
airbnb_df.to_sql('tsla_stocks', conn, index=False, if_exists='replace')
# closing the database connection
conn.close()
