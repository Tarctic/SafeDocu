# from generate_id import result
from pymongo import MongoClient

ids = 0

def create_database(links, result):
    client = MongoClient("mongodb://localhost:27017/")
    db = client["mydatabase"]
    collection = db["files"]
    id = result
    byte_array = id.to_bytes(34, byteorder="big")
    document = {"uid": byte_array, "file": links}
    results = collection.insert_one(document)
    print("Inserted document with ID:", results.inserted_id)
    ress = collection.find()
    byte_array = document["uid"]
    global ids
    ids = int.from_bytes(byte_array, byteorder="big")
    for re in ress:
        print(re)
    print(ids)


def find_user_files():
    client = MongoClient()
    db = client["mydatabase"]
    collection = db[collection]
    user_files = collection.find({"uid": ids})

    for doc in user_files:
        print(doc)
