import json
from itertools import combinations

def jaccard_similarity(set1, set2):
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union != 0 else 0

def find_similar_entries(file_path, threshold=0.8):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    similar_pairs = []
    for (i, list1), (j, list2) in combinations(enumerate(data), 2):
        similarity = jaccard_similarity(set(list1), set(list2))
        if similarity > threshold:
            similar_pairs.append(((i, list1), (j, list2), similarity))
    
    return similar_pairs

def main():
    file_path = "last.json"  # Replace with your JSON file path
    similar_entries = find_similar_entries(file_path)
    
    if similar_entries:
        print("Entries with more than 80% similarity:")
        for (idx1, list1), (idx2, list2), sim in similar_entries:
            print(f"List {idx1} and List {idx2} -> Similarity: {sim:.2%}")
            print(f"List {idx1}: {list1}")
            print(f"List {idx2}: {list2}\n")
    else:
        print("No similar entries found.")

if __name__ == "__main__":
    main()
