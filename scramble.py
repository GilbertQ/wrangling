# Replace 'your_file.txt' with the path to your text file
import re
file_path = 'testing.json'


try:
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            stripped_line = line.strip()
            # Check if the line meets the conditions
            if (stripped_line[1:].startswith("Q") or
                re.match(r"^[ABCDEFGHIJKLMNabcdefghijklmn]\.\s", stripped_line[1:]) or
                stripped_line[1:].startswith("Answ")):
                print(f"{line_number}: {stripped_line}")  # Print line if it meets the condition
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

