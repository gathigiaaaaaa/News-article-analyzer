from analyzer import (
    substring_specific_word_count,
    regex_most_common_word,
    average_word_length,
    count_paragraphs,
    count_sentences
)
from file_handler import load_article


def display_menu():
    print("\n====================================")
    print("      NEWS ARTICLE ANALYZER")
    print("====================================")
    print("1. Substring Match & Specific Word Count")
    print("2. Regex Match & Identify Most Common Word")
    print("3. Calculate Average Word Length")
    print("4. Count Paragraphs")
    print("5. Count Sentences")
    print("6. Exit")


def main():

    article = load_article("../data/article.txt")

    if not article:
        return

    while True:

        display_menu()

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":

            word = input("Enter the word to search: ").strip()

            found, count = substring_specific_word_count(article, word)

            if found:
                print(f'\n"{word}" was found in the article.')
                print(f'It appears {count} time(s).')
            else:
                print(f'\n"{word}" was NOT found in the article.')

            input("\nPress Enter to continue...")

        elif choice == "2":

            word, frequency = regex_most_common_word(article)

            print("\nMost Common Word")
            print("----------------")
            print(f"Word: {word}")
            print(f"Occurrences: {frequency}")

            input("\nPress Enter to continue...")

        elif choice == "3":

            average = average_word_length(article)

            print(f"\nAverage Word Length: {average:.2f}")

            input("\nPress Enter to continue...")

        elif choice == "4":

            paragraphs = count_paragraphs(article)

            print(f"\nParagraph Count: {paragraphs}")

            input("\nPress Enter to continue...")

        elif choice == "5":

            sentences = count_sentences(article)

            print(f"\nSentence Count: {sentences}")

            input("\nPress Enter to continue...")

        elif choice == "6":

            print("\nThank you for using News Article Analyzer!")
            break

        else:

            print("\nInvalid choice. Please enter a number from 1 to 6.")
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()