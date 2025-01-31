import json
import numpy as np
from difflib import SequenceMatcher

def find_similar_strings(data, similarity_threshold=0.8):
    # Convert the JSON to a numpy array
    arr = np.array(data)
    
    # Get the number of sublists and their length
    num_sublists = len(arr)
    sublist_length = len(arr[0]) if num_sublists > 0 else 0
    
    # Store similar strings
    similar_strings = []
    
    # Iterate through each position in the sublists
    for pos in range(sublist_length):
        # Extract strings at this position from all sublists
        strings_at_pos = [sublist[pos] for sublist in arr if pos < len(sublist)]
        
        # Compare each string with others
        for i, str1 in enumerate(strings_at_pos):
            similar_group = [str1]
            for j, str2 in enumerate(strings_at_pos):
                if i != j:
                    # Calculate similarity ratio
                    similarity = SequenceMatcher(None, str1, str2).ratio()
                    if similarity > similarity_threshold:
                        similar_group.append(str2)
            
            # If we found a group of similar strings and it's not already in our results
            if len(similar_group) > 1 and similar_group not in [group for group, _, _ in similar_strings]:
                similarity_percentage = len(similar_group) / num_sublists * 100
                similar_strings.append((similar_group, pos, similarity_percentage))
    
    return similar_strings

# Example usage
# Load the JSON file
with open('last.json', 'r') as file:
    data = json.load(file)

# Find similar strings
similar_strings = find_similar_strings(data)

# Print results
for group, position, percentage in similar_strings:
    print(f"At position {position}:")
    print("Similar strings:", group)
    print(f"Appears in {percentage:.2f}% of sublists")
    print("---")