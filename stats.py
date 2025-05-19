def count_words(content):
    return len(content.split())

def count_characters(text: str) -> dict:
    text = text.lower()
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sorted_dictionary(char_count):
    sorted_list = []

    for char, count in char_count.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_list.append({"char": char, "num": count})

        # Sort the list by count in descending order
    sorted_list.sort(key=lambda x: x["num"], reverse=True)

    return sorted_list