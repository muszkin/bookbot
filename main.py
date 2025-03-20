def get_words_count(text):
    words = text.split()
    return len(words)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    num_words = get_words_count(get_book_text("books/frankenstein.txt"))
    print(f"{num_words} words found in the document")


main()
