import os
import re

def replace_question_numbers(folder_path):
    # Define the regex pattern to match "Question" followed by numbers 1 to 500
    pattern = re.compile(r"Question \d+")

    # Iterate through all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        print(file_path)
        # Process only text files
        if os.path.isfile(file_path) and filename.endswith(".json"):
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            print(content)
            # Replace "Question #" with "Question "
            updated_content = pattern.sub("Question ", content)
            
            # Save the changes back to the file
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            print(f"Processed: {filename}")

# Specify the path to your folder
folder_path = "/home/matabell/Documents/Workspaces/Python/ITIL/output_parts/"  # Replace with the actual folder path
replace_question_numbers(folder_path)

