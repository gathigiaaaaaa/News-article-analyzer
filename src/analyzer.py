import re
from utils import clean_words


def substring_specific_word_count(text, word):
    """
    Checks if a word exists in the article
    and counts how many times it appears.
    """

    words = clean_words(text)

    found = False

    count = 0

    if word.lower() in text.lower():
        found = True

    for item in words:

        if item == word.lower():

            count += 1

    return found, count


def regex_most_common_word(text):
    """
    Uses Regular Expressions to identify
    the most common word.
    """

    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())

    frequency = {}

    for word in words:

        if word in frequency:

            frequency[word] += 1

        else:

            frequency[word] = 1

    most_common = ""
    highest = 0

    for word in frequency:

        if frequency[word] > highest:

            highest = frequency[word]

            most_common = word

    return most_common, highest


def average_word_length(text):
    """
    Calculates average word length.
    """

    words = clean_words(text)

    total_letters = 0

    for word in words:

        total_letters += len(word)

    average = total_letters / len(words)

    return average


def count_paragraphs(text):
    """
    Counts paragraphs.
    """

    paragraphs = [p for p in text.split("\n\n") if p.strip()]

    return len(paragraphs)


def count_sentences(text):
    """
    Counts sentences using regex.
    """

    sentences = re.findall(r"[^.!?]+[.!?]", text)

    return len(sentences)