import sys
if len(sys.argv) == 2:
    exit
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

from stats import word_count

from stats import character_count

from stats import character_sort

def main():
    content = get_book_text(sys.argv[1]) #("books/frankenstein.txt")
    wCount = word_count(content)
    cCount = character_count(content)
    cSort = character_sort(cCount)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {wCount} total words")
    print("--------- Character Count -------")
    for entry in cSort:
        ch = entry["char"]
        if ch.isalpha():
            print(f"{ch}: {entry['num']}")

main()
    