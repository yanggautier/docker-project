import streamlit as st
import pandas as pd
import os 
from pymongo import MongoClient


username = os.environ["MONGO_ROOT_USER"]
password = os.environ["MONGO_ROOT_PASSWORD"]
# Titre de l'application

st.title('Application Streamlit Simple')


try:
    client = MongoClient(f'mongodb://{username}:{password}@mongodb:27017/')
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

