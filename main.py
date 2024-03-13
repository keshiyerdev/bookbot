from collections import Counter

def main():
    book_path = "books/frankenstein.txt"
    text = read_book(book_path)
    word_count = countText(text)
    counter = countLetters(text)
    print(f"{word_count} words found in the document")
    counter = dict(counter.most_common())
    for item in counter:
        if item.isalpha():
            print(f"The letter {item} appears {counter[item]} times!")


def countText(text):
    words = text.split()
    return len(words)

def countLetters(text):
    text = text.lower()
    return Counter(text)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()


main()