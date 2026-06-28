import re


def clean_words(text):
    """
    Removes punctuation and converts all words to lowercase.
    Returns a list of cleaned words.
    """

    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())

    return words