import sys
from stats import create_report


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book = sys.argv[1]
        create_report(book)


main()
