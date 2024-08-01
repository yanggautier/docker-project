from flask import Flask, jsonify
from pymongo import MongoClient
import os 

username = os.environ["MONGO_ROOT_USER"]
password = os.environ["MONGO_ROOT_PASSWORD"]

app = Flask(__name__)

@app.route('/')
def home():
    return "Bonjour, vous pouvez utiliser /books pour récupérer tout les livres dans la bdd !"


@app.route('/books')
def books():
    try:
        client = MongoClient(f'mongodb://{username}:{password}@mongodb:27017/')
        db = client["db"]
        collection = db["books"]
        cursor = collection.find()
        books = list(cursor)

        for book in books:
            book.pop('_id', None)

        return jsonify(books)
    
    except ConnectionError:
        return "Une erreur s'est produite !"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)