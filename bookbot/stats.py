# Count the number of words in the book.
def count_words(text):
    words = text.split()
    return len(words)

# Count characters in the book.
def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def sort_on(item):
	return item["num"]


def report_sort(char_counts):
    new_list = []
    for key in char_counts:
        char = key
        num = char_counts[key]
        new_list.append({"char": char, "num": num})
        new_list.sort(reverse=True, key=sort_on)
    return new_list


    