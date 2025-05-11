def modify_file(input_file_path, output_file_path):
    """
    Reads a file, modifies each line, and writes the modified lines to a new file.

    Args:
        input_file_path (str): The path to the input file.
        output_file_path (str): The path to the output file.
    """
    try:
        # Open the input file in read mode ('r')
        with open(input_file_path, 'r') as infile:
            # Read all lines from the input file into a list
            lines = infile.readlines()

        # Modify each line (example: add line number and reverse the line)
        modified_lines = []
        for i, line in enumerate(lines):
            # Remove trailing newline characters for cleaner manipulation
            line = line.rstrip('\n')
            # Add the line number and reverse the text of each line.
            modified_line = f"{i+1}: {line[::-1]}\n"
            modified_lines.append(modified_line)

        # Open the output file in write mode ('w')
        with open(output_file_path, 'w') as outfile:
            # Write the modified lines to the output file
            outfile.writelines(modified_lines)

        print(f"Successfully modified '{input_file_path}' and saved to '{output_file_path}'")

    except FileNotFoundError:
        print(f"Error: File not found at p")   
