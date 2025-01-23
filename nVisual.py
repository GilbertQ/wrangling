import json

# Function to check if any string in the list contains any of the specified words
def contains_keywords(strings, keywords):
    return any(any(keyword in string for keyword in keywords) for string in strings)

# List of keywords to search for
keywords = [" figure", " picture", " image"]

# Load the JSON file
with open('combined.json', 'r') as file:
    data = json.load(file)

# Lists to store found and remaining records
found_records = []
remaining_records = []

# Iterate through the list and separate elements containing the keywords
for element in data:
    if contains_keywords(element, keywords):
        found_records.append(element)
    else:
        remaining_records.append(element)

# Save the remaining records back to the original JSON file
with open('combined.json', 'w') as file:
    json.dump(remaining_records, file, indent=4)

# Save the found records to a new JSON file
with open('found_records.json', 'w') as file:
    json.dump(found_records, file, indent=4)

# Print the total number of found records
print(f"Total number of found records: {len(found_records)}")
