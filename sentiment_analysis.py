import os
import nltk
from nltk.stem import SnowballStemmer

# Set up the stemmer to extract word roots
stemmer = SnowballStemmer("english")

# Define the lists of word roots to compare frequency against
list0 = ["accommod", "fell","asset purchas","loos","contract","loosen","contractionar","lower","cool", "movedown","cut", "put downward","dampen", "recess","decay", 
"reduc","declin", "reduct","depress", "slack","deterior", "slower","drop", "sluggish","eas", "soft","expansionar","soften","fall", "softer","fallen", "trim", "turndown","weak","weaken","weaker"]
list1 = ["acceler","aggress","aris","arisen","augment","boom","bubbl","caution","cautious","climb","destabilis","expand","gain","goup","hawkin","hike", "increas","lift", "tighten","tighter","moveup", "unsustain","moveupward" 
"upturn","overheat","pickup","pressur","putupward","rais","rise","risen","rose","strengthen","strong","stronger","tight"]

# Define a function to extract word roots from a text string
def extract_roots(text):
    tokens = nltk.word_tokenize(text.lower())
    roots = [stemmer.stem(token) for token in tokens]
    return roots

# Set up a directory path containing the .txt files to analyze
dir_path = "https://github.com/tricarico672/Capstone_Text_Analysis/tree/main/txt%20statements"

# Iterate through each .txt file in the directory and assign a score
for filename in os.listdir(dir_path):
    if filename.endswith(".txt"):
        with open(os.path.join(dir_path, filename), "r") as file:
            text = file.read()
            roots = extract_roots(text)
            freq1 = sum([1 for root in roots if root in list1])
            freq0 = sum([1 for root in roots if root in list0])
            if freq1 > freq0:
                score = 1
            else:
                score = 0
            print(f"{filename}: {score}")
