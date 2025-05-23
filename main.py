from stats import get_book_text, sort_char_count
import sys

def main():
    if len(sys.argv) < 2:
        raise Exception("Usage: python3 main.py <path_to_book>")
    else:

        file = sys.argv[1]
        word_count = get_book_text(file)
        char_list = sort_char_count(file)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at books/{file}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for set in char_list:
            print(f"{set['char']}: {set['num']}")
        print("============= END ===============")


main()
