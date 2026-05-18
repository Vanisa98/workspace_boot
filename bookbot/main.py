# Ensure that the correct number of arguments is provided 
import sys

if len(sys.argv) != 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

## Import functions from other files
from stats import count_words
from stats import get_chars_dict
from stats import report_sort

# main() function shows the overall information.
def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = get_chars_dict(text)
    char_sort = report_sort(char_count)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print(f"--------- Character Count -------")
    for item in char_sort:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print(f"============= END ===============")


# get_book_text() function that reads the text of the book and returns it as a string.
def get_book_text(path):
     with open(path) as f:
        return f.read()

main()