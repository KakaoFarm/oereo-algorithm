# bronze 1
import sys


def main():
    numbers = number_inputer()
    results = is_palindrome_number(numbers)
    result_printer(results)


def is_palindrome_number(numbers):
    result = list()
    flag = True
    for number in numbers:
        flag = True
        for char_index in range(len(number)):
            if number[char_index] != number[len(number) - char_index -1]:
                flag = False
        if flag is False:
            result.append("no")
        else:
            result.append("yes")
    return result


def number_inputer():
    data = ""
    numbers = list()
    while data != "0":
        data = sys.stdin.readline().rstrip()
        if data != "0":
            numbers.append(data)
    return numbers


def result_printer(results):
    for result in results:
        print(result)


main()