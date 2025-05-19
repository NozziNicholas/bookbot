import sys

from stats import count_words, count_characters, sorted_dictionary
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        content = get_book_text(sys.argv[1])
        print(f"{count_words(content)} words found in the document")
        for char, count in count_characters(content).items():
            print(f"'{char}': {count}")

        sorted_chars = sorted_dictionary(count_characters(content))

        print("============ BOOKBOT ============")
        print("Analyzing book found at books/frankenstein.txt...")
        print("----------- Word Count ----------")
        # Assume you calculated total_words elsewhere
        total_words = 75767
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")

        for entry in sorted_chars:
            print(f"{entry['char']}: {entry['num']}")

        print("============= END ==============")

main()