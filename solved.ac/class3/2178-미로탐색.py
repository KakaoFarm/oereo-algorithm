import sys
from collections import deque

row, col = map(int, input().split())

miro = [[0] * col for _ in range(row)]
visited = [[0] * col for _ in range(row)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(row):
    row = sys.stdin.readline().rstrip()
    for j in range(col):
        miro[i][j] = int(row[j])


def bfs(x, y, miro):
    queue = deque()
    queue.append((x, y))
    miro[x][y] = 0
    visited[x][y] = 1

    while queue:

        x, y = queue.popleft()
        if x == len(miro) - 1 and y == len(miro[0]) - 1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_out_range_in_miro(nx, ny, len(miro), len(miro[0])):
                continue
            if miro[nx][ny] != 0 and visited[nx][ny] == 0:
                miro[nx][ny] = 0
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    print(visited[len(miro) - 1][len(miro[0]) - 1])


def is_out_range_in_miro(x, y, row, col):
    return x < 0 or y < 0 or x >= row or y >= col


bfs(0, 0, miro)
