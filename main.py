def main():
    book_location = "books/frankenstein.txt" # stores the book's relative path in a variable
    text = read_book(book_location)
    word_count = count_words(text)
    result = count_characters(text)
    converted = convert_dict(result)
    formatted_output = format_output(converted, book_location, word_count)

    
# format the output and remove non-alpha characters
def format_output(ordered_dict, path_to_book, counted_words):
    print(f'--- Begin report of {path_to_book}---')
    print(f'{counted_words} words found in the document\n')
    for char_entry in ordered_dict:
        for key in char_entry:
            if key.isalpha():
                count = char_entry[key]
                print(f'The "{key}" character was found {count} times.')
    print("--- End report ---")

# convert dictionary to list of tuples and sort it, then convert back to sorted list of dictionaries
def convert_dict(dic):
    to_tuples = list(dic.items())
    to_tuples.sort(reverse=True, key=lambda item: item[1])
    
    ordered_dict = [{k:v} for k, v in to_tuples]
    return ordered_dict


# count character occurances
def count_characters(text):
    character_count = {}
    for character in text.lower():
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return character_count
 

# counts the number of words in the book
def count_words(text):
    count = 0
    for word in text.split():
        count += 1
    return count

# opens the text file, reads it, and returns text
def read_book(path):
    with open(path) as f:
        return f.read()


main()