# A-B bronze5

def calculate_minus():
    first_number, second_number = get_numbers()
    return first_number - second_number


def get_numbers():
    first_number, second_number = map(int, input().split())
    return first_number, second_number


print(calculate_minus())
