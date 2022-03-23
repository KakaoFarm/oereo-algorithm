import sys
from collections import deque
from pprint import pprint

col, row, height = map(int, input().split())

dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [1, -1, 0, 0, 0, 0]

tomato_map = [[[0] * col for _ in range(row)] for _ in range(height)]
visited_map = [[[0] * col for _ in range(row)] for _ in range(height)]

for i in range(height):
    for j in range(row):
        case = list(map(int, sys.stdin.readline().rstrip().split()))
        for k in range(col):
            tomato_map[i][j][k] = case[k]


def bfs(after_tomatoes):
    queue = deque()
    for after_tomato in after_tomatoes:
        queue.append(after_tomato)
    cnt = 0
    while queue:
        x, y, z = queue.popleft()
        cnt += 1
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if not is_not_out_of_range(nx, ny, nz):
                continue
            if tomato_map[nz][nx][ny] == 0 and visited_map[nz][nx][ny] == 0:
                queue.append((nx, ny, nz))
                tomato_map[nz][nx][ny] = 1
                visited_map[nz][nx][ny] = visited_map[nz - dz[i]][nx - dx[i]][ny - dy[i]] + 1


def is_not_out_of_range(x, y, z):
    return 0 <= x < row and 0 <= y < col and 0 <= z < height


result = 0
after_tomatoes = []

hidden_case_cnt = 0

for i in range(height):
    for j in range(row):
        for k in range(col):
            if tomato_map[i][j][k] == 0:
                hidden_case_cnt += 1
            if tomato_map[i][j][k] == 1:
                after_tomatoes.append((j, k, i))

if hidden_case_cnt == 0:
    result = 0
else:
    bfs(after_tomatoes)
    for i in range(height):
        for j in range(row):
            for k in range(col):
                if tomato_map[i][j][k] == 0:
                    result = -1
                    break
                result = max(result, max(visited_map[i][j]))

print(result)
