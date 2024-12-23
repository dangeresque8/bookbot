# print("hello world")

# book = "books/frankenstein.txt"
def main():
    path = "books/frankenstein.txt"
    book_text = get_text(path)
    word_ct = get_word_ct(book_text)
    letter_dic = letter_ct(book_text)
    letter_list_dict = sort_dict(letter_dic)
    make_report(word_ct, letter_list_dict)


def get_word_ct(text):
    words = text.split()
    # print(f"{len(words)} words fount in document")
    return len(words)

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def letter_ct(book):
    letter = {}
    file_lower = book.lower()

    for words in file_lower:
        for w in words:
            if w in letter:
                letter[w] += 1
            else:
                letter[w] = 1
    return letter


def sort_dict(dict):
    sorted = []
    for key in dict:
        list_of_dict = {}
        list_of_dict["char"] = key
        list_of_dict["count"] = dict[key]
        sorted.append(list_of_dict)
    sorted.sort(reverse=True, key=sort_on)
    # print(sorted)
    return sorted

def sort_on(dict):
    return dict["count"]

def make_report(ct, list_dict):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{ct} words found in the document\n")
    for d in list_dict:
        if d["char"].isalpha() == True:
            print(f"The '{d["char"]}' character was found {d["count"]} times")
    print("--- End report ---")


main()
