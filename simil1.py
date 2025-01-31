import json
import numpy as np
from collections import defaultdict

def group_similar_string_groups(data, similarity_threshold=0.8):
    # Group sublists based on their content
    grouped_data = defaultdict(list)
    
    # Iterate through each sublist in the data
    for idx, sublist in enumerate(data):
        # Convert the sublist to a tuple of strings for hashability
        key = tuple(sorted(sublist))
        grouped_data[key].append(idx)
    
    # Find groups with high similarity
    similar_groups = []
    for group, indices in grouped_data.items():
        # Calculate the percentage of sublists in this group
        similarity_percentage = len(indices) / len(data) * 100
        
        # If the group appears in more than the threshold percentage
        if similarity_percentage > similarity_threshold * 100:
            similar_groups.append({
                'group': list(group),
                'indices': indices,
                'percentage': similarity_percentage
            })
    
    return similar_groups

# Load the JSON file
with open('last.json', 'r') as file:
    data = json.load(file)

# Find similar groups
similar_groups = group_similar_string_groups(data)

# Print results
for group_info in similar_groups:
    print("Similar Group of Strings:", group_info['group'])
    print("Appears in indices:", group_info['indices'])
    print(f"Appears in {group_info['percentage']:.2f}% of sublists")
    print("---")