from collections import deque
from pprint import pprint
from itertools import permutations

decos =[2,3]*6
grid =["###.#","..#.#","###.#","#..##","###.."]
result = 5

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

#      2 /   3
# 3  ,    2  / 2
# 2  /   2,3    / 2
# 2  / 3,2 / 2   / 2

minimum_number = min(decos)
print(minimum_number)


def dfs(numbers, target):
    answer = 0
    queue = deque()
    queue.append((numbers[0], 0))
    n = len(numbers)
    while queue:
        temp, idx = queue.popleft()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer


def main():
    room_map = [[0] * len(grid) for _ in range(len(grid))]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            room_map[i][j] = grid[i][j]

    pprint(room_map)
    print(dfs(decos, 11))

main()






# 11개면은 홀수다. 2,3으로 만들 수 있는 갯수는 3 2 2 2 2 / 3 3 3 2