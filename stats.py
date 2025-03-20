def get_words_count(text):
    words = text.split()
    return len(words)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def count_chars(text):
    chars = {}
    for letter in text:
        small_letter = letter.lower()
        if small_letter in chars:
            chars[small_letter] += 1
        else:
            chars[small_letter] = 1
    return chars


def sort_on(dic):
    return dic["count"]


def print_list(l):
    s = ""
    for el in l:
        letter = el["letter"]
        count = el["count"]
        s += f"{letter}: {count}\n"
    return s[:-1]

def create_report(book):
    text = get_book_text(book)
    num_words = get_words_count(text)
    letter_count = count_chars(text)
    sorted_list = []
    for letter in letter_count:
        if letter.isalpha():
            sorted_list.append({"letter": letter, "count": letter_count[letter]})
    sorted_list.sort(reverse=True, key=sort_on)
    sorted_list_string = print_list(sorted_list)
    print(f"""
    ============ BOOKBOT ============
Analyzing book found at {book}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------
{sorted_list_string}
============= END ===============
    """)
