import os
from web3 import Web3, HTTPProvider
from web3.contract import ConciseContract

# Connect to the Goerli test network using Infura
infura_url = "https://goerli.infura.io/v3/ddca8499dc454347a7fa460096535d24"
web3 = Web3(HTTPProvider(infura_url))
from web3 import Web3

address = "0xf5a21117f5e0fF05DdF5C0626f8edDCe1486eE1e"
# connect to a local Ethereum node

# Set the account address and private key for signing transactions
account_address = "0x69c14cc30C634F79A07a3BFed69ff11B095Cb099"
private_key = "ef2896b12a2a55194fcb02c91848483ccd2f1a21b39dc86a536d3aaac87c918c"
# web3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# set the account to use for the transaction
# web3.eth.default_account = web3.eth.accounts[0]

# get the contract instance
contract_address = "0xf5a21117f5e0fF05DdF5C0626f8edDCe1486eE1e"
contract_abi = [
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "fileId",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "input1",
                "type": "string",
            },
            {
                "indexed": False,
                "internalType": "string",
                "name": "input2",
                "type": "string",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "integer1",
                "type": "uint256",
            },
            {
                "indexed": False,
                "internalType": "bytes[]",
                "name": "fileInputs",
                "type": "bytes[]",
            },
            {
                "indexed": False,
                "internalType": "uint256",
                "name": "timestamp",
                "type": "uint256",
            },
        ],
        "name": "FilesProcessed",
        "type": "event",
    },
    {
        "inputs": [
            {"internalType": "string", "name": "input1", "type": "string"},
            {"internalType": "string", "name": "input2", "type": "string"},
            {"internalType": "uint256", "name": "integer1", "type": "uint256"},
            {"internalType": "bytes[]", "name": "fileInputs", "type": "bytes[]"},
        ],
        "name": "processFiles",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "name": "fileRecords",
        "outputs": [
            {"internalType": "string", "name": "input1", "type": "string"},
            {"internalType": "string", "name": "input2", "type": "string"},
            {"internalType": "uint256", "name": "integer1", "type": "uint256"},
            {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "string", "name": "input1", "type": "string"},
            {"internalType": "string", "name": "input2", "type": "string"},
            {"internalType": "uint256", "name": "integer1", "type": "uint256"},
            {"internalType": "bytes[]", "name": "fileInputs", "type": "bytes[]"},
        ],
        "name": "generateFilesID",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "string", "name": "input1", "type": "string"},
            {"internalType": "string", "name": "input2", "type": "string"},
            {"internalType": "uint256", "name": "integer1", "type": "uint256"},
        ],
        "name": "generateID",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [{"internalType": "uint256", "name": "fileId", "type": "uint256"}],
        "name": "getFileRecord",
        "outputs": [
            {
                "components": [
                    {"internalType": "string", "name": "input1", "type": "string"},
                    {"internalType": "string", "name": "input2", "type": "string"},
                    {"internalType": "uint256", "name": "integer1", "type": "uint256"},
                    {
                        "internalType": "bytes[]",
                        "name": "fileInputs",
                        "type": "bytes[]",
                    },
                    {"internalType": "uint256", "name": "timestamp", "type": "uint256"},
                ],
                "internalType": "struct FileProcessor.FileRecord",
                "name": "",
                "type": "tuple",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getTotalFilesProcessed",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalFilesProcessed",
        "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
        "stateMutability": "view",
        "type": "function",
    },
]
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# call the generateID function
input1 = "hello"
input2 = "world"
age = 25
file_inputs = [b"file1", b"file2"]

# input1 = input("Enter Name: ")
# input2 = input("Enter Gender: ")
# age = int(input("Enter age: "))
# num_files = int(input("Enter the number of file inputs: "))
# file_inputs = [
#     input(f"Enter file input {i}: ").encode() for i in range(1, num_files + 1)
# ]

result = contract.functions.generateFilesID(input1, input2, age, file_inputs).call()
# print the result to the console
print("Unique ID:", result)
