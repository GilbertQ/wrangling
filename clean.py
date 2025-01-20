def clean_text(text):
    # Keep only alphanumeric characters, spaces, periods, and question marks
    # Also preserve 'A.', 'B.', 'C.', 'D.' at the start of lines
    if text.startswith(('A.', 'B.', 'C.', 'D.')):
        option = text[:2]  # Keep the letter and period
        text = text[2:]    # Process the rest of the line
        # Keep alphanumeric, spaces, periods, and question marks
        cleaned = ''.join(char for char in text if char.isalnum() or char in ' .?')
        return option + cleaned
    else:
        return ''.join(char for char in text if char.isalnum() or char in ' .?')

def process_text_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            lines = f.readlines()

        # Remove blank lines and strip whitespace
        lines = [line.strip() for line in lines if line.strip()]

        processed_lines = []
        current_option = []
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            # Handle question numbers
            if line.startswith('QUESTION'):
                processed_lines.append(clean_text(line))
                i += 1
                continue
            
            # Handle answer lines
            if line.startswith('Correct Answer:'):
                line = line.replace('Correct Answer:', 'Answer:')
                if not line.endswith('.'):
                    line += '.'
                processed_lines.append(clean_text(line))
                i += 1
                continue
            
            # Handle options (starting with capital letter + point)
            if line[0].isupper() and len(line) > 1 and line[1] == '.':
                current_option = [line]
                i += 1
                while i < len(lines):
                    next_line = lines[i]
                    if (next_line[0].isupper() and len(next_line) > 1 and next_line[1] == '.') or \
                       next_line.startswith('Answer:') or \
                       next_line.startswith('Correct Answer:') or \
                       next_line.startswith('QUESTION'):
                        break
                    current_option.append(next_line)
                    i += 1
                joined_option = ' '.join(current_option)
                processed_lines.append(clean_text(joined_option))
                continue
            
            # Handle other lines
            processed_lines.append(clean_text(line))
            i += 1

        # Write processed lines to output file
        with open(output_file, 'w') as f:
            f.write('\n'.join(processed_lines))
            
        print(f"File processed successfully. Output written to {output_file}")
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage
input_file = "itil1.txt"
output_file = "output.txt"
process_text_file(input_file, output_file)