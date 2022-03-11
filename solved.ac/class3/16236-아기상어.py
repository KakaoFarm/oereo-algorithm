import sys
from collections import deque

N = int(input())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 맵 세팅
shark_map = [[0] * N for _ in range(N)]

for i in range(N):
    row = sys.stdin.readline().rstrip().split()
    for j in range(N):
        shark_map[i][j] = int(row[j])


def bfs(x, y, shark_size):
    queue = deque()
    queue.append((x, y))
    bite_fishes = list()
    visited_map = [[0] * N for _ in range(N)]
    visited_map[x][y] = 0

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if is_out_range_in_map(nx, ny, len(shark_map), len(shark_map[0])):
                continue
            if is_visited(nx, ny, visited_map):
                continue
            if shark_map[nx][ny] <= shark_size:
                visited_map[nx][ny] = 1 + visited_map[x][y]
                queue.append((nx, ny))
                if shark_map[nx][ny] < shark_size and shark_map[nx][ny] != 0:
                    bite_fishes.append([nx, ny, visited_map[nx][ny]])

    return bite_fishes


def is_out_range_in_map(x, y, row, col):
    if x < 0 or y < 0 or x >= row or y >= col:
        return True


def is_visited(x, y, visited_map):
    return visited_map[x][y] != 0


def game_start(i, j):
    shark_size = 2
    timer = 0
    size_up_count = 0

    while 1:
        bite_fishes = bfs(i, j, shark_size)
        bite_fishes.sort(key=lambda x: (-x[2], -x[0], -x[1]))

        # 물고기 없을때
        if len(bite_fishes) == 0:
            break

        bite_fish = bite_fishes.pop()
        timer += bite_fish[2]
        size_up_count += 1
        shark_map[i][j] = 0
        shark_map[bite_fish[0]][bite_fish[1]] = 0
        i = bite_fish[0]
        j = bite_fish[1]

        if size_up_count == shark_size:
            shark_size += 1
            size_up_count = 0

    print(timer)


for i in range(N):
    for j in range(N):
        if shark_map[i][j] == 9:
            game_start(i, j)
