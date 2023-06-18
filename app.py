# import uuid
# from flask import Flask, request
# from flask_smorest import abort
# from db import items, stores

# app = Flask(__name__)


# @app.get("/store")  # http://127.0.0.1:5000/store
# def get_stores():
#     return {"stores": list(stores.values())}


# @app.post("/store")
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     store = {**store_data, "id": store_id}
#     stores[store_id] = store
#     return store, 201


# @app.post("/item")
# def create_item():
#     item_data = request.get_json()
#     if item_data["store_id"] not in stores:
#         abort(
#             404, message="Store not found."
#         )  ### when we finish flask smorest application, this will take care of documenting error options

#     item_id = uuid.uuid4().hex
#     item = {**item_data, "id": item_id}
#     items[item_id] = item

#     return item, 201


# @app.get("/store/<string:store_id>")
# def get_store(store_id):
#     try:
#         print(stores)
#         return stores[store_id]
#     except KeyError:
#         abort(404, message="Store not found.")


# @app.get("/item/<string:item_id>")
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message="Item not found.")


# @app.get("/item")
# def get_all_items():
#     return {"items": list(items.values())}


from flask import Flask, request


app = Flask(__name__)

stores = [{"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]}]


@app.get("/store")  # http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}


@app.post("/store")  # http://127.0.0.1:5000/store
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    return new_store, 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>/item")
def get_item_in_store(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found"}, 404
