# 두 수 비교하기 브로즈4

def main():
    numbers = get_numbers()
    if numbers[0] > numbers[1]:
        return ">"
    if numbers[0] < numbers[1]:
        return "<"
    if numbers[0] == numbers[1]:
        return "=="


def get_numbers():
    numbers = list(map(int, input().split()))
    return numbers


print(main())