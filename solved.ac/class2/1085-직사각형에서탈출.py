# bronze3

def main():
    indexes = get_square_information()
    start_point = [0, 0]

    return is_minimum_distance(start_point, indexes)


def is_minimum_distance(start_point, indexes):
    x_gap = min(abs(start_point[0] - indexes[0]), abs(indexes[0]-indexes[2]))
    y_gap = min(abs(start_point[1] - indexes[1]), abs(indexes[1] - indexes[3]))
    return min(x_gap, y_gap)


def get_square_information():
    index = list(map(int, input().split()))
    return index


print(main())