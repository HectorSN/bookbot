import sys
from stats import get_book_text, count_words, conteo, order_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        ruta_libro = sys.argv[1]
        text = get_book_text(ruta_libro)
        num_words = count_words(text)
        chars = conteo(text)  
        count = order_count(chars)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {ruta_libro}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        for d in count:
            print((f"{d['char']}: {d['num']}"))

        print("============= END ===============")
    

