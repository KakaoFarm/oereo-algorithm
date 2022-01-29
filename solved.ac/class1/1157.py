# 단어 공부 브론즈1

def main():
    chars = get_sentence()
    char_dictionary = count_char(chars)

    return get_most_used_char(char_dictionary)


def get_sentence():
    words = list(input().upper())
    return words


def get_most_used_char(char_dictionary:dict):
    sorted_chars = sorted(char_dictionary.items(), reverse=True, key=lambda item: item[1])
    if len(sorted_chars) == 1:
        return sorted_chars[0][0]
    if is_unique(sorted_chars[0][1], sorted_chars[1][1]):
        return sorted_chars[0][0]
    return "?"


def is_unique(first_index, second_index):
    if first_index == second_index:
        return False
    return True


def count_char(chars:list):
    char_dictionary = dict()
    for char in chars:
        if char not in char_dictionary.keys():
            char_dictionary[char] = 1
        elif char in char_dictionary.keys():
            char_dictionary[char] = char_dictionary[char]+1
    return char_dictionary

print(main())