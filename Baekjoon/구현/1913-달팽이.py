from pprint import pprint

n = int(input())
value = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

snail_map = [[0] * n for _ in range(n)]


def dfs(x, y, cnt):
    stack = []
    stack.append((x,y))
    snail_map[x][y] = cnt

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_out_range(nx, ny):
                continue
            if snail_map[nx][ny] == 0:
                stack.append((nx, ny))
                snail_map[nx][ny] = snail_map[x][y] +1
                pprint(snail_map)


def is_out_range(x, y):
    return x < 0 or y < 0 or x >= n or y >= n

snail_map[0][0] = 1
dfs(0, 0, 1)
pprint(snail_map)
