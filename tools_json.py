
import json


FILE_PATH = 'data.json'

def load_data():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

