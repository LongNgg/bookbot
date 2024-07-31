def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        chars = count_characters(file_contents)
        chars.sort(reverse=True, key=sort_on)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")

        for char in chars:
            if char["char"].isalpha():
                print(f"The '{char['char']}' character was found {char['count']} times")
        print("--- End report ---")


def count_words(s):
    words = s.split()
    # print(len(words))
    return len(words)


def count_characters(s):
    s = s.lower()
    char_count = {}
    for char in s:
        tmp_dict = {}
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    list_chars = [{"char": key, "count": value} for key, value in char_count.items()]
    return list_chars


def sort_on(dict):
    return dict["count"]


main()
