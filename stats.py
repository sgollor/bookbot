def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def sort_on(item):
    return item["num"]

def sort_character_counts(char_counts):
    sorted_list = []

    for char in char_counts:
        if char.isalpha():
            sorted_list.append({
                "char": char,
                "num": char_counts[char]
            })

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
