import os

# Directory where the text files are located
dir_path = '/Users/anthony/Desktop/Spring 2023/EC 480/Capstone Ideas/Datasets/text analysis/txt statements'

# Iterate over each file in the directory
for file_name in os.listdir(dir_path):
    if file_name.endswith('.txt'):  # Check that the file is a text file
        # Open the file and read its contents
        with open(os.path.join(dir_path, file_name), 'r') as f:
            lines = f.readlines()

        # Strip the first 6 lines
        stripped_lines = lines[6:]

        # Write the stripped lines back to the file
        with open(os.path.join(dir_path, file_name), 'w') as f:
            f.writelines(stripped_lines)
