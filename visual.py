import json

# Function to check if any string in the list contains any of the specified words
def contains_keywords(strings, keywords):
    return any(any(keyword in string for keyword in keywords) for string in strings)

# List of keywords to search for
keywords = [" figure", " picture", " mage"," drag"]

# Load the JSON file
with open('Qc.json', 'r') as file:
    data = json.load(file)
# Counter for the number of found records
found_count = 0

# Iterate through the list and display elements containing the keywords
for element in data:
    if contains_keywords(element, keywords):
        print(element)
        found_count += 1

# Print the total number of found records
print(f"Total number of found records: {found_count}")