with open("books/frankenstein.txt") as f:
    text = f.read()
    lowered_text = text.lower()

def sort_on(character_count):
    return character_count["num"]

def main():
    
    words = text.split()
    word_count = len(words)
        
    
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


    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    
    print("--- End report ---")
           
if __name__ == "__main__":
    main()
