import os

# Directory where the text files are located
dir_path = "/Users/anthony/Desktop/Spring 2023/EC 480/Capstone Ideas/Datasets/text analysis/stripped statements"

# Loop over each file in the directory
for filename in os.listdir(dir_path):
    if filename.endswith(".txt"):
        # Open the file and read its contents
        with open(os.path.join(dir_path, filename), "r") as f:
            lines = f.readlines()

        # Remove the last 35 lines from the list of lines
        stripped_lines = lines[:-35]

        # Write the stripped lines back to the file
        with open(os.path.join(dir_path, filename), "w") as f:
            f.writelines(stripped_lines)
