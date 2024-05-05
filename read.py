import json

def read_lands_data(file_path):
    try:
        with open(file_path, 'r') as file:
            lands_data = json.load(file)
        return lands_data
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except json.JSONDecodeError:
        print("Error: JSON decoding failed.")
        return None
