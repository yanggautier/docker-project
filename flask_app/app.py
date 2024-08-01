from flask import Flask, jsonify
from pymongo import MongoClient
import os 

mongo_uri = os.environ["MONGO_URI"]

app = Flask(__name__)

@app.route('/')
def home():
    return "Bonjour, vous pouvez utiliser /books pour récupérer tout les livres dans la bdd !"


@app.route('/books')
def books():
    try:
        client = MongoClient(mongo_uri)
        db = client["db"]
        collection = db["books"]
        cursor = collection.find({}, {'_id': 0})
        books = list(cursor)
        return jsonify(books)
    
    except ConnectionError:
        return "Une erreur s'est produite !"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)