import os
from pdfminer.high_level import extract_text

# Define input and output directories
input_dir = "Your/Directory"
output_dir = "Your/Directory"

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".pdf"):
        # Extract the text from the PDF file
        text = extract_text(os.path.join(input_dir, filename))
        # Write the text to a new text file
        with open(os.path.join(output_dir, f"{filename[:-4]}.txt"), "w") as text_file:
            text_file.write(text)
