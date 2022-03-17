import sys

n = int(input())
paper_map = [[0] * n for _ in range(n)]

for i in range(n):
    row = sys.stdin.readline().rstrip().split()
    for j in range(n):
        paper_map[i][j] = int(row[j])

blue_paper_count = 0
white_paper_count = 0

# print(paper_map)


def dfs(n, paper_map):
    global blue_paper_count
    global white_paper_count
    cnt = 0
    for i in range(n):
        cnt += sum(paper_map[i])

    if cnt == 0:
        white_paper_count += 1
    elif cnt == n * n:
        blue_paper_count += 1

    else:
        dfs(n // 2, [paper_map[i][0:n // 2] for i in range(n // 2)])
        dfs(n // 2, [paper_map[i][n // 2:n] for i in range(n // 2)])
        dfs(n // 2, [paper_map[i][0:n // 2] for i in range(n // 2, n)])
        dfs(n // 2, [paper_map[i][n // 2:n] for i in range(n // 2, n)])
    # print(white_paper_count)
    return white_paper_count, blue_paper_count


white_paper_count, blue_paper_count = dfs(n, paper_map)
print(white_paper_count)
print(blue_paper_count)
