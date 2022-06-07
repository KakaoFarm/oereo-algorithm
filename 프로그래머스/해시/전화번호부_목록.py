import random


def solution(phone_book):
    answer = True
    phones = dict()
    phone_book.sort(key=lambda item: len(item))

    for i in range(len(phone_book)):
        for j in phone_book[i + 1:]:
            # print(j, phone_book[i])
            if j.startswith(phone_book[i]):
                print(phone_book)
    return answer