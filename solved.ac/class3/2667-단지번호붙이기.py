import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
N = int(input())
complex_map = [[0] * N for _ in range(N)]

for i in range(N):
    row = sys.stdin.readline().rstrip()
    for j in range(N):
        complex_map[i][j] = int(row[j])


def bfs_map(complex_map, x, y):
    queue = deque()
    queue.append((x, y))
    complex_map[x][y] = 0
    cnt = 0

    while queue:
        cnt +=1
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_out_range_in_map(nx, ny, len(complex_map), len(complex_map[0])):
                continue
            if complex_map[nx][ny] == 1:
                complex_map[nx][ny] = 0
                queue.append((nx, ny))
    return cnt


def is_out_range_in_map(x, y, row, col):
    if x < 0 or y < 0 or x >= row or y >= col:
        return True

complex_count = 0
complex_map_cnt = []

for i in range(len(complex_map)):
    for j in range(len(complex_map[i])):
        if complex_map[i][j] == 1:
            cnt = bfs_map(complex_map, i, j)
            complex_map_cnt.append(cnt)
            complex_count +=1

print(complex_count)
complex_map_cnt.sort()
for complex_map in complex_map_cnt:
    print(complex_map)