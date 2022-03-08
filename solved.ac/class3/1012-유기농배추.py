from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def main():
    cabbage_maps = init()

    for cabbage_map in cabbage_maps:
        cnt = 0
        for i in range(len(cabbage_map)):
            for j in range(len(cabbage_map[0])):
                if cabbage_map[i][j] == 1:
                    bfs(cabbage_map, i, j)
                    cnt += 1

        print(cnt)


def bfs(cabbage_map, x, y):
    queue = deque()
    queue.append((x, y))
    cabbage_map[x][y] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_out_range_in_map(nx, ny, len(cabbage_map), len(cabbage_map[0])):
                continue
            if cabbage_map[nx][ny] == 1:
                cabbage_map[nx][ny] = 0
                queue.append((nx, ny))
    return


def is_out_range_in_map(x, y, row, col):
    if x < 0 or y < 0 or x >= row or y >= col:
        return True


def init():
    cabbage_maps = list()
    n = int(input())

    for case in range(n):
        row, col, earth_worm_count = map(int, input().split())
        cabbage_map = [[0] * row for _ in range(col)]
        for earth_worm in range(earth_worm_count):
            x, y = map(int, input().split())
            cabbage_map[y][x] = 1
        cabbage_maps.append(cabbage_map)

    return cabbage_maps


main()
