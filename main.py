from flask import Flask
import pymongo
from pymongo import MongoClient

import json
from bson import json_util

app = Flask(__name__)

cluster =MongoClient("mongodb+srv://rupesh:abcd611@cluster0.zidic.mongodb.net/Bollywood?retryWrites=true&w=majority")

db=cluster["Bollywood"]
collection=db["Drugged"]


collection.insert_many( [ { "name":"deepika", "drugged":"yes" }, { "name":"shahrukh", "drugged":"no" } ]   )

app= Flask(__name__)
@app.route("/Drugged",methods=["GET"])
def get_names():
    all_stars= list(collection.find({}))
    return json.dumps(all_stars,default=json_util.default)

if __name__ == "__main__":
    app.run()