def load_article(file_path):
    """
    Loads and returns the contents of the article file.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            article = file.read()

        return article

    except FileNotFoundError:

        print("Error: article.txt was not found.")

        return ""