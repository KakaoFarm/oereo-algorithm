import sys
from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append(end)
    graph[end].append(start)


# print(graph)

def bfs(point, visited):
    queue = deque()
    queue.append(point)
    visited[point] = True

    while queue:
        n_point = queue.pop()
        for next_point in graph[n_point]:
            if not visited[next_point]:
                queue.append(next_point)
                visited[next_point] = True


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        bfs(i, visited)
        cnt += 1
print(cnt)
