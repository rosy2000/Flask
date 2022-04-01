from cgitb import reset
from hashlib import new
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

##POST -> Receive data
##GET -> To send data
stores = [
    {
        "name": "WalMart",
        "items": [{"Cloths" : "Shorts ", "price": 99}],
        "Discount": 0,
    },
    {
        "name": "Reliance",
        "items": [{"Cloths" : "Tops ", "price": 100}],
        "Discount": 10,
    },
]


# POST /store data : {name:}
##ADD new store
@app.route("/store", methods=["POST"])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": [],"Discount":request_data["Discount"]}
    stores.append(new_store)
    return jsonify(new_store)


# GET details of a perticular store
@app.route("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store)
    return jsonify({"Message": "Store not found!"})


# GET details of all stores.
@app.route("/store")
def get_stores():
    return jsonify({"Stores": stores})


## POST append item to existing store.
@app.route("/store/<string:name>/item", methods=["POST"])
def create_items_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if (store["name"] == name):
            new_item = {"Cloths": request_data["Cloths"], "price": request_data["price"]}
        store["items"].append(new_item)
        return jsonify(new_item)
    return jsonify({"Message": "Store not found!"})


## GET items of a perticular store.
@app.route("/store/<string:name>/item")
def get_items_in_store(name):
    for store in stores:
        if store["name"] == name:
            return jsonify(store["items"])
    return jsonify({"Message": "Store not found!"})


app.run(port=1234)