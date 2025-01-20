import json

# Load the JSON data
with open('data.json', 'r') as file:
    data = json.load(file)

# Initialize a variable to store the sum of the third field
total = 0

# Loop through each record and add the value of the third field (convert it to float)
for record in data:
    try:
        # Convert the third field to float (it may contain decimals)
        total += float(record[2])  # Assuming the third field is at index 2 (0-based index)
    except ValueError:
        # If the conversion fails, skip the record or handle it as needed
        print(f"Skipping invalid value for record: {record}")

# Print the total sum of the third field
print(f'The total of the third field is: {total}')
