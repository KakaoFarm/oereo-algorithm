# silver 5

def main():
    number = inputer()
    result = get_666_number(number)
    return result


def get_666_number(number):
    flag = 0
    compare_number = 0

    while flag != number:
        if "666" in str(compare_number):
            flag = flag+1
        compare_number = compare_number +1
    return compare_number - 1



def inputer():
    return int(input())


print(main())