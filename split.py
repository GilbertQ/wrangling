import json
import os

# Load the JSON file
input_file = 'itil.json'  # Replace with your JSON file name
output_folder = 'output_parts'  # Folder to save the split files
num_parts = 4  # Number of parts to split into

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Read the JSON data
with open(input_file, 'r') as f:
    data = json.load(f)

# Ensure the data is a list
if not isinstance(data, list):
    raise ValueError("The JSON file does not contain a list.")

# Calculate the split size
split_size = len(data) // num_parts
remainder = len(data) % num_parts

# Split the data
start_index = 0
for i in range(num_parts):
    # Determine the end index for the current part
    end_index = start_index + split_size + (1 if i < remainder else 0)
    part_data = data[start_index:end_index]

    # Save the current part to a new JSON file
    output_file = os.path.join(output_folder, f'part_{i + 1}.json')
    with open(output_file, 'w') as f:
        json.dump(part_data, f, indent=4)
    
    start_index = end_index


print(f"Data split into {num_parts} parts and saved in '{output_folder}' folder.")
