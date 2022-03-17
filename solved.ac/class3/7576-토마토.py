import sys
from collections import deque
from pprint import pprint

col, row = map(int, input().split())

tomato_map = [[0] * col for _ in range(row)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(row):
    input_data = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(col):
        tomato_map[i][j] = input_data[j]


# pprint(tomato_map)

def bfs(tomatoes):
    queue = deque()
    for tomato in tomatoes:
        queue.append(tomato)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_out_range(nx, ny):
                continue
            if tomato_map[nx][ny] == 0:
                tomato_map[nx][ny] = tomato_map[x][y] + 1
                queue.append((nx, ny))


def is_out_range(x, y):
    return x < 0 or y < 0 or x >= row or y >= col


tomato_count = 0
tomatoes = []
for i in range(row):
    for j in range(col):
        if tomato_map[i][j] == 1:
            tomato_count += 1

            tomatoes.append((i, j))
bfs(tomatoes)


def check_un_tomato():
    for i in range(row):
        for j in range(col):
            if tomato_map[i][j] == 0:
                return -1


if tomato_count == (row * col):
    print(0)
elif check_un_tomato() == -1:
    print(-1)
else:
    print(max(map(max, tomato_map)) - 1)
