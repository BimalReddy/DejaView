import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import logging

# Ensure required NLTK datasets are downloaded 
# (quiet=True prevents it from spamming your terminal every time it runs)
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('wordnet', quiet=True)
except Exception as :
    logging.warning(f"Could not download NLTK data: {e}")

def preprocess_text(text):
    """
    Cleans raw text by lowercasing, removing punctuation, 
    filtering out stopwords, and lemmatizing the remaining words.
    """
    if not text:
        return ""

    # 1. Lowercase everything (so "Apple" and "apple" match)
    text = text.lower()
    
    # 2. Remove punctuation using regex (replaces commas, periods, etc. with a space)
    text = re.sub("[{re.escape(string.punctuation)}]", " ", text)
    
    # 3. Tokenize (split the giant string into a list of individual words)
    tokens = word_tokenize(text)
    
    # 4. Remove stopwords (filler words) and Lemmatize (find the root word)
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    
    cleaned_tokens = [
        lemmatizer.lemmatize(word) 
        for word in tokens 
        # Only keep the word if it's not a stopword and not just a number
        if word not in stop_words and not word.isdigit()
    ]
    
    # 5. Join the clean tokens back into a single string separated by spaces
    return " ".join(cleaned_tokens)

# Quick test block (runs only if you execute this specific file directly)
if __name__ == "__main__":
    sample_text = "The quick brown foxes are jumping over the lazy dogs! 123"
    print(f"Original: {sample_text}")
    print(f"Cleaned:  {preprocess_text(sample_text)}")
