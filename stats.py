def word_count(text):
    num_words = len(text.split())
    return num_words

def letter_count(text):
    char_frequencies = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_frequencies:
            char_frequencies[lowered] += 1
        else:
            char_frequencies[lowered] = 1

    return char_frequencies

def sort_on(d):
    return d["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list