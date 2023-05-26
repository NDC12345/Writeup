import requests
import json

import json
from base64 import b64encode
import hashlib

username = "admin"
users = {
    "username": "admin"
}

def hash(data):
    return hashlib.sha256(data.encode('utf-8')).hexdigest()

data = {
    "username": username,
    "user_type": "premium"
}

b64data = b64encode(json.dumps(data).encode()).decode()
# data_hash = hash(b64data + users[username])

print("Encoded Data:", b64data)
# print("Data Hash:", data_hash)