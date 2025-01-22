import json

def count_json_records(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    if isinstance(data, list):
        return len(data)
    else:
        return 1


record_count = count_json_records('qsc.json')
print(f"The JSON file contains {record_count} record(s).")
