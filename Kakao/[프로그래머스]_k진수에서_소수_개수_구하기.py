import math


def solution(n, k):
    answer = 0
    total_number = convert_number(int(str(n), 10), k)
    splited_number = total_number.split("0")

    for number in splited_number:
        if number != '' and number != '1' and is_prime_number(int(number)):
            answer += 1
    return answer


def convert_number(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]


def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
        if str(x).find("0") != -1:
            return False
    return True
