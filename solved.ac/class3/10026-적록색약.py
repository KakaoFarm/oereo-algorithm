import sys
from collections import deque

N = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

normal_people_map = [["0"] * N for _ in range(N)]
not_normal_people_map = [["0"] * N for _ in range(N)]

for i in range(N):
    row = str(sys.stdin.readline().rstrip())
    for j in range(N):
        normal_people_map[i][j] = row[j]
        not_normal_people_map[i][j] = row[j]
        if row[j] == "G":
            not_normal_people_map[i][j] = "R"

# print(normal_people_map)
# print(not_normal_people_map)


def bfs(people_map, x, y, char_type):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_out_range_in_map(nx, ny, len(people_map), len(people_map[0])):
                continue
            if people_map[nx][ny] == char_type:
                people_map[nx][ny] = "0"
                queue.append((nx, ny))
    return


def is_out_range_in_map(x, y, row, col):
    if x < 0 or y < 0 or x >= row or y >= col:
        return True


cnt_1 = 0
cnt_2 = 0

for i in range(N):
    for j in range(N):
        if normal_people_map[i][j] != "0":
            bfs(normal_people_map, i, j, normal_people_map[i][j])
            cnt_1 += 1
        if not_normal_people_map[i][j] != "0":
            bfs(not_normal_people_map, i, j, not_normal_people_map[i][j])
            cnt_2 += 1

print(cnt_1, cnt_2)
