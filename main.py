def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_dict = get_char_count(book_text)
    char_list = get_sorted_alpha_char_list(char_dict)
    print_report(num_words, char_list)


def sort_on(dict):
    return dict['num']

def print_report(num_words, char_list):
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{num_words} words found in the document\n")
    for char in char_list:
        print(f"The {char['name']} character was found {char['num']} times")
    print("--- End of Report --")

def get_sorted_alpha_char_list(char_dict):
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append({'name': char, 'num': char_dict[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list


def get_char_count(text):
    char_dict = {}
    for char in text:
        lower_char = char.lower()
        char_dict[lower_char] = char_dict.get(lower_char, 0) + 1
    return char_dict

def get_num_words(text):
    return len(text.split())

def get_book_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

main()
