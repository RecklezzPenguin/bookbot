def main():
    path = "books/frankenstein.txt"
    words = get_text_of_book(path)
    num_of_words = num_of_words_in_book(words)
    character_dictionary = num_of_times_character_appears(words)
    book_report_list = character_dictionary_in_sorted_list(character_dictionary)

    #Book Report

    print(f"--- Begin report of {path} ---")
    print(f"{num_of_words} words found in the document")
    print("")

    for character in book_report_list:
        alpha = character["character"].isalpha()
        if alpha:
            print(f"The '{character['character']}' character was found {character['num']} times")

    print("--- End report ---")

def sort_on(dict):
    return dict["num"]

def character_dictionary_in_sorted_list(character_dictionary):
    sorted_list_of_characters = []
    for character in character_dictionary:
        sorted_list_of_characters.append({"character": character, "num": character_dictionary[character]})
    sorted_list_of_characters.sort(reverse=True, key=sort_on)
    return sorted_list_of_characters

def num_of_words_in_book(book):
    words = book.split()
    return len(words)

def get_text_of_book(path):
    with open(path) as f:
        return f.read()
    
def num_of_times_character_appears(text):
    characters = {}
    for string in text:
        lowered_string = string.lower()
        if lowered_string in characters:
            characters[lowered_string] += 1
        else:
            characters[lowered_string] = 1
    return characters

main()