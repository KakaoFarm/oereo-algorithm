import sys

n = int(input())
video_map = [[0] * n for _ in range(n)]

for i in range(n):
    row = sys.stdin.readline().rstrip()
    for j in range(n):
        video_map[i][j] = int(row[j])

# print(video_map)


def dfs(n, video_map, depth):
    cnt = 0
    for i in range(n):
        cnt += sum(video_map[i])
    # print(cnt)
    if cnt == 0:
        print(0, end="")
    elif cnt == n * n:
        print(1, end="")

    else:
        print("(", end="")
        dfs(n // 2, [video_map[i][0:n // 2] for i in range(n // 2)], depth)
        dfs(n // 2, [video_map[i][n // 2:n] for i in range(n // 2)], depth)
        dfs(n // 2, [video_map[i][0:n // 2] for i in range(n // 2, n)], depth)
        dfs(n // 2, [video_map[i][n // 2:n] for i in range(n // 2, n)], depth)
        print(")", end="")


dfs(n, video_map, 0)
