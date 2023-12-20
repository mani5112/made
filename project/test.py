import unittest
import logging
import os
import sqlite3
import pandas as pd


class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        logging.info("setting up the data")
        try:
            # Set up SQLite databases
            self.tweet_db_path = '../data/elon_tweets.sqlite'
            self.conn1 = sqlite3.connect(self.tweet_db_path)
            self.query1 = f"SELECT * FROM elon_tweets;"
            self.df_tweets = pd.read_sql_query(self.query1, self.conn1)

            self.tsla_stock_db_path = '../data/tsla_stocks.sqlite'
            self.conn2 = sqlite3.connect(self.tsla_stock_db_path)
            self.query2 = f"SELECT * FROM tsla_stocks;"
            self.tsla_stocks_df = pd.read_sql_query(self.query2, self.conn2)
        except Exception as e:
            self.fail(f"Failed to set up: {e}")

    def test_tweets_database(self):
        logging.info("Running elon tweets database...")
        try:
            # Test if the elon_tweets table exists in the database
            cursor = self.conn1.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            self.assertIn('elon_tweets', table_names)
            print("Test passed: elon_tweets table exists in the database.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_test_stock_database(self):
        logging.info("checking tesla stock database...")
        try:
            # Test if the tsla_stocks table exists in the database
            cursor = self.conn2.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            table_names = [table[0] for table in tables]
            self.assertIn('tsla_stocks', table_names)
            print("Test passed: tsla_stocks table exists in the database.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_df_tweets(self):
        logging.info("checking test_hotel_bookings_dataframe...")
        try:
            # Test if the df_tweets DataFrame is not empty
            self.assertFalse(self.df_tweets.empty)
            print("Test passed: df_tweets DataFrame is not empty.")
        except Exception as e:
            self.fail(f"Test failed: {e}")

    def test_tsla_stocks_dataframe(self):
        logging.info("Running tsla_stocks dataframe...")
        try:
            # Test if the tsla_stocks_df DataFrame is not empty
            self.assertFalse(self.tsla_stocks_df.empty)
            print("Test passed: tsla_stocks_df DataFrame is not empty.")
        except Exception as e:
            self.fail(f"Test failed: {e}")


if __name__ == '__main__':
    unittest.main()
