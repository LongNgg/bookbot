def main():
    # Use a context manager to handle file opening and closing
    file_path = "books/frankenstein.txt"
    with open(file_path) as f:
        file_contents = f.read()

    # Calculate word count and character count
    word_count = count_words(file_contents)
    chars = count_characters(file_contents)

    # Sort characters by count in descending order
    chars.sort(key=lambda x: x["count"], reverse=True)

    # Generate the report
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    for char in chars:
        if char["char"].isalpha():  # Check if character is alphabetic
            print(f"The '{char['char']}' character was found {char['count']} times")

    print("--- End report ---")


def count_words(s):
    """Count the number of words in a string."""
    words = s.split()
    return len(words)


def count_characters(s):
    """Count the occurrences of each character in a string."""
    s = s.lower()
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Convert char_count dictionary to a list of dictionaries
    list_chars = [{"char": key, "count": value} for key, value in char_count.items()]
    return list_chars


main()
