import os
import ipfshttpclient
from database import create_database
# import generate_id
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract
from pymongo import MongoClient
from bson.binary import Binary
from contract_abi import contract_abi

from flask import Flask, redirect, request, render_template, session, url_for


app = Flask(__name__)
app.secret_key = "wiehfoiwhelskndf23hohfoish"

@app.route("/")
def index():
    return render_template("index.html")

# Connect to the Goerli test network using Infura
infura_url = "https://goerli.infura.io/v3/ddca8499dc454347a7fa460096535d24"
web3 = Web3(HTTPProvider(infura_url))

address = "0xf5a21117f5e0fF05DdF5C0626f8edDCe1486eE1e"
# connect to a local Ethereum node

# Set the account address and private key for signing transactions
account_address = "YOUR_ACCOUNT_ADDRESS"
private_key = "YOUR_PRIVATE_KEY"

# get the contract instance
contract_address = "0xf5a21117f5e0fF05DdF5C0626f8edDCe1486eE1e"
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

client = ipfshttpclient.connect()

links = ""

@app.route("/uploader", methods=["POST","GET"])
def upload_files():
    hlink = "https://ipfs.io/ipfs/"
    if request.method == 'POST':
        files = request.files.getlist("files")
        name = request.form["name"]
        email = request.form["email"]
        age = int(request.form["age"])
        file_inputs = []
        for file in files:
            file_inputs.append(bytes(file.filename, "utf-8"))
            res = client.add(file)
            print(res)
            print("Hash: ", res.get("Hash"))
            hlink += res.get("Hash")
            print("The link: ", hlink)
            global links
            links = hlink
        result = contract.functions.generateFilesID(name, email, age, file_inputs).call()
        create_database(links, result)
    return render_template("success.html", link=hlink)


if __name__ == "__main__":
    app.run()
    
