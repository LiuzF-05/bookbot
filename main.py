from stats import count_words, count_chars, sorting
import sys
def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else: 
        path=sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {count_words(path)} total words")
    print("--------- Character Count -------")
    for pair in (sorting(count_chars(path))):
        print (f"{pair['char']}: {pair['num']}")
    print("============= END ===============")
main()
