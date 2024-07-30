def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        chars = count_characters(file_contents)

        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document")
        for char in chars.sort():
            print(f"The '{char}' character was found {chars[char]} times")
        print("--- End report ---")
        # print(file_contents)


def count_words(s):
    words = s.split()
    # print(len(words))
    return len(words)


def count_characters(s):
    char_count = {}
    for char in s.lower():
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count


main()
