from pprint import pprint

city_count = int(input())

case = int(input())
max_num = 10 ** 9 + 1
city_map = [[max_num] * (city_count + 1) for _ in range(city_count + 1)]

for i in range(1, city_count + 1):
    for j in range(1, city_count + 1):
        if i == j:
            city_map[i][j] = 0

for i in range(case):
    start, end, cost = map(int, input().split())
    city_map[start][end] = min(city_map[start][end], cost)

for i in range(1, city_count + 1):
    for j in range(1, city_count + 1):
        for k in range(1, city_count + 1):
            city_map[j][k] = min(city_map[j][k], city_map[j][i] + city_map[i][k])

for i in range(1, city_count + 1):
    for j in range(1, city_count + 1):
        if city_map[i][j] == max_num:
            city_map[i][j] = 0
        print(city_map[i][j], end=" ")
    print()
