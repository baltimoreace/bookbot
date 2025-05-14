import sys

from stats import get_num_words

def sort_on(character_count):
        return character_count["num"]

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    with open(file_path) as f:
        text = f.read()
        lowered_text = text.lower()

    word_count = get_num_words(text)
    character_count = {}
    for characters in lowered_text:
        if characters in character_count:
            character_count[characters] += 1
        else:
            character_count[characters] = 1

    char_list = []
    for char, count in character_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    char_list.sort(reverse=True, key=sort_on)


    print("--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    
    for item in char_list:
        print(f"{item['char']}: {item['num']}")
    
    print("--- End report ---")
           
if __name__ == "__main__":
    main()
