import json
import random

def scramble_and_renumber(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        data = json.load(file)
    
    # Iterate over each question block
    for question in data:
        # Extract options and answer
        options = [line for line in question if line[0] in "ABCDEFGHIJ" and line[1] == '.']
        answer_line = next((line for line in question if line.startswith("Answer:")), None)
       
        if answer_line:
            # Extract correct answers (letters) from the answer line
            correct_answers = answer_line.split(": ")[1][:-1].split(", ")
            # Scramble the options
            print(options)

            # Create a mapping from old letter (A., B., etc.) to new number (1., 2., etc.)
            letter_to_new_number = {options[i][0]: f"{i + 1}" for i in range(len(options))}
            print(letter_to_new_number)
            random.shuffle(options)
            print(options)
# Update the options with new numbering
            for i, option in enumerate(options):
                new_prefix = f"{i + 1}."
                options[i] = new_prefix + option[2:]  # Replace the old prefix (A., B., etc.) with the new one (1., 2., etc.)
            print(options)
            # Convert back from 1., 2., 3., etc. to A., B., C., etc.
            number_to_letter = {f"{i + 1}": chr(65 + i) for i in range(len(options))}
            for i, option in enumerate(options):
                letter_prefix = number_to_letter[str(i + 1)]
                options[i] = letter_prefix + ". " + option[3:]  # Replace the numeric prefix with the corresponding letter
            
            # Update the answer line to reflect letter prefixes
            new_answer = ", ".join([number_to_letter[letter_to_new_number[letter]] for letter in correct_answers]) + "."
            answer_line_index = question.index(answer_line)
            question[answer_line_index] = f"Answer: {new_answer}"
            
            # Replace the old options with the new, scrambled, and letter-renumbered options
            option_indices = [i for i, line in enumerate(question) if line[0] in "ABCDEFGHIJ" and line[1] == '.']
            for i, index in enumerate(option_indices):
                question[index] = options[i]
    
    # Save the modified data to the output file
    with open(output_filename, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
scramble_and_renumber('testing.json', 'qsc.json')



