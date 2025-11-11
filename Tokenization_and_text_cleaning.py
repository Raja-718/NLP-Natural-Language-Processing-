# Text Cleaning and Tokenization Experiment

import re
import string

# Sample dataset (you can replace with file or online dataset later)
texts = [
    "I love Natural Language Processing! It's amazing to see how computers understand text.",
    "Machine Learning and Deep Learning are revolutionizing many fields, including healthcare and finance.",
    "Data preprocessing is an essential step before building any ML model.",
    "Tokenization splits sentences into words, making text easier to analyze.",
    "Cleaning text involves removing punctuation, numbers, and converting to lowercase."
]

# Cleaning Function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.strip()
    return text

# Tokenization Function
def tokenize(text):
    return text.split()

# Process data
for i, t in enumerate(texts):
    cleaned = clean_text(t)
    tokens = tokenize(cleaned)
    
    print(f"\n------- SAMPLE {i+1} -------")
    print("Original Text:")
    print(t)
    print("\nCleaned Text:")
    print(cleaned)
    print("\nTokenized Text:")
    print(tokens)
