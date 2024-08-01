from pymongo import MongoClient
import os
import pandas as pd

mongo_uri = os.environ["MONGO_URI"]

def insert_data(file_path):
    try:
        client = MongoClient(mongo_uri)
        db = client["db"]
        books = db["books"]

        df = pd.read_csv(file_path)
        books_df = df.to_dict('records')
        result = books.insert_many(books_df)
        print(f"Inserted {len(result.inserted_ids)} documents into MongoDB")
        client.close()
        
    except ConnectionError:
        raise "An exception occurred"
