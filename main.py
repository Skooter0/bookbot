def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    character_dict = get_characters(text)
    character_sorted_list = character_dict_to_sorted_list(character_dict)

    print (f"--- Begin report of {book_path} ---")
    print (f"{num_words} words fount in the document")
    print ()

    for item in character_sorted_list:
        if not item["char"].isalpha():
            continue
        print (f"The '{item['char']}' character was fount {item['num']} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(d):
    return d["num"]

def character_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

main()