def reverse_file_content(input_file, output_file):
    # Open the input file and read its contents
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Reverse the order of the lines
    reversed_lines = lines[::-1]
    
    # Open the output file and write the reversed lines
    with open(output_file, 'w') as file:
        file.writelines(reversed_lines)

# Specify the input and output file names
input_file = 'input.txt'
output_file = 'output.txt'

# Call the function to reverse the content
reverse_file_content(input_file, output_file)

print(f"Reversed content has been saved to {output_file}.")
