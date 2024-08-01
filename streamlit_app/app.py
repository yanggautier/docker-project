import streamlit as st
import pandas as pd
import os 
from pymongo import MongoClient


mongo_uri = os.environ["MONGO_URI"]

st.title('Application Streamlit Simple')


try:
    client = MongoClient(mongo_uri)
    db = client["db"]
    books = db["books"]
    # Fetch all documents from the collection
    cursor = books.find()
    # Convert cursor to list of dictionaries
    data = list(cursor)
    # Create pandas DataFrame
    df = pd.DataFrame(data)

    # Drop the MongoDB-generated '_id' column if not needed
    df = df.drop('_id', axis=1)
    client.close()
    st.write(f"Nombre de livre dans la base de données {len(df)}")
    st.table(df)

except ConnectionError:
    raise "An exception occurred"

