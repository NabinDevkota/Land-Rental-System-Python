import json

def read_lands_data():
    with open('lands_data.json', 'r') as file:
        lands_data = json.load(file)
    return lands_data
