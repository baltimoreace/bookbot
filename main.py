def count_words(file_path):
    with open(file_path) as f:
        text = f.read()
    words = text.split()
    return len(words)

def main():
    word_count = count_words("books/franenstein.txt")
    print(word_count)
    
if __name__ == "__main__":
    main()
    