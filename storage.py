import json
import os
from cryptography.fernet import Fernet

FILE_PATH = "clipboard_history.enc"
KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        return generate_key()

    with open(KEY_FILE, "rb") as f:
        return f.read()
    
def save_history(history):
    key = load_key()
    fernet = Fernet(key)

    data = json.dumps(history).encode()
    encrypted = fernet.encrypt(data)

    with open(FILE_PATH, "wb") as f:
        f.write(encrypted)


def load_history():
    if not os.path.exists(FILE_PATH):
        return []

    key = load_key()
    fernet = Fernet(key)

    try:
        with open(FILE_PATH, "rb") as f:
            encrypted = f.read()

        decrypted = fernet.decrypt(encrypted)
        return json.loads(decrypted.decode())

    except Exception:
        return []

def add_item(item):
    history = load_history()

    if item and (len(history) == 0 or history[0] != item):
        history.insert(0, item)

    save_history(history)


def get_all():
    return load_history()