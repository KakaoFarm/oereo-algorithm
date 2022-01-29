# silver 5

def main():
    words = get_words()
    remove_duplicated_words = remove_duplicate_word(words);
    sorted_words = sorting_about_word_length(remove_duplicated_words)
    printer(sorted_words)


def sorting_about_word_length(words):
    words.sort(key=lambda x: (len(x), x))
    return words


def remove_duplicate_word(words):
    return list(set(words))


def get_words():
    total_word_count = int(input())
    words = list()
    for i in range(total_word_count):
        words.append(input())
    # words = list(map(str, input().split('\n')))
    return words


def printer(words):
    for word in words:
        print(word)


main()