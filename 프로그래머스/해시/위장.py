def solution(clothes):
    answer = 0
    clothes_map = dict()
    for clothes_set in clothes:
        clothes_name = clothes_set[0]
        clothes_index = clothes_set[1]
        if clothes_index not in clothes_map:
            clothes_map[clothes_index] = 1
        else:
            clothes_map[clothes_index] += 1

    result = 1
    for index, value in clothes_map.items():
        result *= (value + 1)
    answer = result - 1
    return answer