import re


def get_article():
    """
    Allows the user to paste a news article.
    Type END on a new line when finished.
    """

    print("\nPaste your news article below.")
    print("When you are finished, type END on a new line.\n")

    lines = []

    while True:

        line = input()

        if line.upper() == "END":
            break

        lines.append(line)

    article = "\n".join(lines)

    return article


def clean_words(text):
    """
    Returns a list of cleaned words.
    """

    words = re.findall(r"\b[a-zA-Z']+\b", text.lower())

    return words


def substring_specific_word_count(text, word):
    """
    Performs substring matching and counts
    the number of occurrences.
    """

    found = False

    if word.lower() in text.lower():
        found = True

    words = clean_words(text)

    count = 0

    for item in words:

        if item == word.lower():

            count += 1

    return found, count


def regex_most_common_word(text):
    """
    Finds the most common word using regex.
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
    Calculates the average word length.
    """

    words = clean_words(text)

    total = 0

    for word in words:

        total += len(word)

    return total / len(words)


def count_paragraphs(text):
    """
    Counts paragraphs.
    """

    paragraphs = [p for p in text.split("\n\n") if p.strip()]

    return len(paragraphs)


def count_sentences(text):
    """
    Counts sentences.
    """

    sentences = re.findall(r"[^.!?]+[.!?]", text)

    return len(sentences)


def display_menu():
    print("\n===================================")
    print("      NEWS ARTICLE ANALYZER")
    print("===================================")
    print("1. Substring Match & Specific Word Count")
    print("2. Regex Match & Most Common Word")
    print("3. Average Word Length")
    print("4. Count Paragraphs")
    print("5. Count Sentences")
    print("6. Exit")
def main():
    article = get_article()

    if article.strip() == "":
        print("No article was entered.")
        return

    while True:

        display_menu()

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":

            word = input("Enter the word to search: ")

            found, count = substring_specific_word_count(article, word)

            if found:
                print(f'\n"{word}" was found.')
                print(f'Occurrences: {count}')
            else:
                print(f'\n"{word}" was not found.')

            input("\nPress Enter to continue...")

        elif choice == "2":

            word, frequency = regex_most_common_word(article)

            print("\nMost Common Word")
            print("---------------------")
            print(f"Word: {word}")
            print(f"Occurrences: {frequency}")

            input("\nPress Enter to continue...")

        elif choice == "3":

            average = average_word_length(article)

            print(f"\nAverage Word Length: {average:.2f}")

            input("\nPress Enter to continue...")

        elif choice == "4":

            paragraphs = count_paragraphs(article)

            print(f"\nParagraphs: {paragraphs}")

            input("\nPress Enter to continue...")

        elif choice == "5":

            sentences = count_sentences(article)

            print(f"\nSentences: {sentences}")

            input("\nPress Enter to continue...")

        elif choice == "6":

            print("\nThank you for using News Article Analyzer!")
            break

        else:

            print("\nInvalid choice. Please enter a number from 1 to 6.")

            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()