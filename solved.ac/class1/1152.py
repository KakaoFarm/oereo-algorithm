# 단어의 개수 브로즈2

def main():
    words = get_sentence()
    return len(words)


def get_sentence():
    words = list(map(str, input().split()))
    return words


print(main())