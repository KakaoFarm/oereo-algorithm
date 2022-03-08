# silver 1
import sys
from collections import deque

q = deque();
q.append((0,0))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def main():
    base_map, row, col = map_inputer()
    distance = bfs(base_map, row, col)
    return distance


def bfs(base_map, row, col):
    distance_checking_map = base_map
    while q:
        k = q.popleft()
        for i in range(4):
            x = k[0] + dx[i]
            y = k[1] + dy[i]
            if 0<=x<row and 0<=y<col and base_map[x][y] == 1:
                base_map[x][y] = 1
                distance_checking_map[x][y] = (distance_checking_map[k[0]][k[1]]) + 1
                q.append((x,y))
    return distance_checking_map


def map_inputer():
    row, col = map(int, input().split())
    base_map = [list(sys.stdin.readline().rstrip()) for i in range(row)]
    # for row in range(row):
    #     base_map[row].append(list(map(int, input().split(""))))
    return base_map, row, col


print(main())