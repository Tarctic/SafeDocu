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