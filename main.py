def main():
    book_location = "books/frankenstein.txt" # stores the book's relative path in a variable
    text = read_book(book_location)
    word_count = count_words(text)
    print("The total amount of words in this book is", word_count)

# opens the text file, reads it, and returns text
def read_book(path):
    with open(path) as f:
        return f.read()

# counts the number of words in the book
def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

main()