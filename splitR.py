import json
import os
import random

# Load the JSON file
input_file = 'last.json'  # Replace with your JSON file name
output_folder = 'output_parts'  # Folder to save the split files
num_parts = 2  # Number of parts to split into

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the JSON data
with open(input_file, 'r') as f:
    data = json.load(f)

# Ensure the data is a list
if not isinstance(data, list):
    raise ValueError("The JSON file does not contain a list.")

# Shuffle the data to ensure randomness
random.shuffle(data)

# Split the data randomly into parts
split_data = [[] for _ in range(num_parts)]
for i, item in enumerate(data):
    split_data[i % num_parts].append(item)

# Save each part to a new JSON file
for i, part_data in enumerate(split_data):
    output_file = os.path.join(output_folder, f'part_{i + 1}.json')
    with open(output_file, 'w') as f:
        json.dump(part_data, f, indent=4)

print(f"Data randomly split into {num_parts} parts and saved in '{output_folder}' folder.")
