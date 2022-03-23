import copy
import sys
from collections import deque

row, col = map(int, input().split())

virus_map = [[0] * col for _ in range(row)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

result = 0

for i in range(row):
    input_row = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(len(input_row)):
        virus_map[i][j] = input_row[j]


def go_virus():
    temp_virus_map = copy.deepcopy(virus_map)
    queue = deque(get_viruses(temp_virus_map))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_out_range(nx, ny):
                continue
            if temp_virus_map[nx][ny] == 0:
                temp_virus_map[nx][ny] = 2
                queue.append((nx, ny))

    calculate_max_live_space_count(temp_virus_map)


def calculate_max_live_space_count(virus_case_map):
    global result
    cnt = 0
    for i in range(row):
        cnt += virus_case_map[i].count(0)
    result = max(result, cnt)


def is_out_range(x, y):
    return x < 0 or y < 0 or x >= row or y >= col


def get_viruses(temp_virus_map):
    viruses = []
    for i in range(row):
        for j in range(col):
            if temp_virus_map[i][j] == 2:
                viruses.append((i, j))
    return viruses


def make_wall(wall_count):
    if wall_count == 3:
        go_virus()
        return
    else:
        for i in range(row):
            for j in range(col):
                if virus_map[i][j] == 0:
                    virus_map[i][j] = 1
                    make_wall(wall_count + 1)
                    virus_map[i][j] = 0


make_wall(0)
print(result)
