from stats import get_num_words
from stats import r_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    d=sys.argv[1]
    
    z=r_dict(d)
    z = dict(sorted(z.items(), key=lambda item: item[1], reverse=True))

    #print(z)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {d}...")
    print("----------- Word Count ----------")
    s=get_num_words(d)
    print(f"Found {s} total words")
    print("--------- Character Count -------")
    for key,value in z.items():
        print(f"{key}: {value}")
    #print(sys.argv)
# Prints ['main.py']
main()
