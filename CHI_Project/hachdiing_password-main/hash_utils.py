import hashlib
import json
import os


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return {}  
