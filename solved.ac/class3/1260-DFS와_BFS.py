from collections import deque

N, case, start_point = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for case_number in range(case):
    row, col = map(int, input().split())
    graph[row].append(col)
    graph[col].append(row)

for edge in graph:
    edge.sort()

visited_dfs = [False for _ in range(len(graph) + 1)]
result_dfs = list()


def dfs(graph, root):
    # visited = [False for _ in range(len(graph) +1)]
    visited_dfs[root] = True

    # stack = [root]
    result_dfs.append(root)
    for i in graph[root]:
        if not visited_dfs[i]:
            dfs(graph, i)

    # while stack:
    #     n = stack.pop()
    #     result.append(n)
    #     for i in graph[n]:
    #         if not visited[i] and graph[n][i] != 0:
    #             visited[i] = True
    #             stack.append(i)

    return result_dfs


def bfs(graph, root):
    result = list()

    visited = [False for _ in range(len(graph) + 1)]
    visited[root] = True
    queue = deque([root])

    while queue:
        n = queue.popleft()
        result.append(n)
        for i in graph[n]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

    return result


for i in range(len(dfs(graph, start_point))):
    print(dfs(graph, start_point)[i], end=' ')
print()
for i in range(len(bfs(graph, start_point))):
    print(bfs(graph, start_point)[i], end=' ')

# print(dfs(graph, start_point))
# print(bfs(graph, start_point))
