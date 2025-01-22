import json
import random

def scramble_and_renumber(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        data = json.load(file)
    
    for question in data:
        # Extract options (lines starting with A., B., etc.)
        options = [line for line in question if line[0] in "ABCDEFGHIJ" and line[1] == '.']
        
        # If there are no options, skip to the next question
        if not options:
            continue
        
        # Extract the answer line
        answer_line = next((line for line in question if line.startswith("Answer:")), None)
        
        if answer_line:
            # Extract correct answers (letters) from the answer line
            correct_answers = answer_line.split(": ")[1].rstrip('.').split(", ")
            
            # Shuffle the options
            random.shuffle(options)
            
            # Map old letters (A., B., etc.) to new ones
            new_letter_map = {options[i][0]: chr(65 + i) for i in range(len(options))}
            
            # Update options with new letter prefixes
            options = [f"{new_letter_map[option[0]]}. {option[3:]}" for option in options]
            
            # Update the answer line with the new letter mapping
            new_answers = [new_letter_map[answer] for answer in correct_answers]
            new_answer_line = f"Answer: {', '.join(new_answers)}."
            
            # Replace the options and answer line in the question
            option_indices = [i for i, line in enumerate(question) if line[0] in "ABCDEFGHIJ" and line[1] == '.']
            for i, index in enumerate(option_indices):
                question[index] = options[i]
            
            if answer_line:
                answer_index = question.index(answer_line)
                question[answer_index] = new_answer_line

    # Save the updated data to the output file
    with open(output_filename, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
scramble_and_renumber('part_1.json', 'qsc1.json')
scramble_and_renumber('part_2.json', 'qsc2.json')
scramble_and_renumber('part_3.json', 'qsc3.json')
scramble_and_renumber('part_4.json', 'qsc4.json')
