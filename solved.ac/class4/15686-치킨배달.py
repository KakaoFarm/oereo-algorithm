import sys
from itertools import permutations, combinations

n, m = map(int, input().split())

chicken_map = []
chicken_houses = []
houses = []

for i in range(n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    chicken_map.append(row)

for i in range(n):
    for j in range(n):
        if chicken_map[i][j] == 2:
            chicken_houses.append((i, j))
        if chicken_map[i][j] == 1:
            houses.append((i, j))

# print(chicken_houses)
# print(chicken_map)


def go_chicken():
    picked_chicken_houses = pick_chicken_houses()
    result = float('inf')
    for chicken_houses_combination in picked_chicken_houses:
        temp = 0

        for house in houses:
            min_house = []
            for chicken_house in chicken_houses_combination:
                min_house.append(abs(house[0] - chicken_house[0]) + abs(house[1] - chicken_house[1]))
            temp += min(min_house)
            # print(temp)
            if result <= temp: break
        if temp < result: result = temp
        # print(result)
    print(result)


def pick_chicken_houses():
    picked_chicken_houses = list(combinations(chicken_houses, m))
    return picked_chicken_houses


go_chicken()