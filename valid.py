import json

def load_json_safely(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        print(f"Error occurs at line {e.lineno}, column {e.colno}")
        return None

# Usage
data = load_json_safely('last.json')