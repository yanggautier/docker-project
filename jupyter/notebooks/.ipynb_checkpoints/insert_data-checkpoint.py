from pymongo import MongoClient
import os
import pandas as pd

username = os.environ["MONGO_ROOT_USER"]
password = os.environ["MONGO_ROOT_PASSWORD"]

def insert_data(file_path):
    try:
        client = MongoClient(f'mongodb://{username}:{password}@mongodb:27017/')
        db = client["db"]
        books = db["books"]

        df = pd.read_csv(file_path)
        books_df = df.to_dict('records')
        result = books.insert_many(books_df)
        print(f"Inserted {len(result.inserted_ids)} documents into MongoDB")
        client.close()
        
    except ConnectionError:
        raise "An exception occurred"
