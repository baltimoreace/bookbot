with open("books/frankenstein.txt") as f:
    text = f.read()
    lowered_text = text.lower()


def main():
    character_count = {}
    for characters in lowered_text:
        if characters in character_count:
            character_count[characters] += 1
        else:
            character_count[characters] = 1

    print(character_count)

           
if __name__ == "__main__":
    main()
