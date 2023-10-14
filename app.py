import sys, json, os
from flask import Flask
from datetime import datetime
from openai.embeddings_utils import get_embedding, cosine_similarity
from pymongo.mongo_client import MongoClient

app = Flask(__name__)

uri = "mongodb+srv://admin:@hackathon.otz1cym.mongodb.net/?retryWrites=true&w=majority"
default_json = {
        "dateTime": datetime.now(),
        "phoneNo": "+16788973910",
        "entry": "Hey! This is a test journal entry. I'm feeling really good today; I just fixed a huge bug in my app.",
    }

@app.route('/')
def index():
    journal_entry = default_json["entry"]
    entry_embedding = get_embedding(journal_entry, engine="text-embedding-ada-002")
    return "hello world 2"

@app.route('/test')
def test():
    return "text"