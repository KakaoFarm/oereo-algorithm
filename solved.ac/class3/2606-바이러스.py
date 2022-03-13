computer_cnt = int(input())
case = int(input())

graph = dict()

def dfs(graph, start_node):
    visited = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return visited


for i in range(computer_cnt):
    graph[str(i+1)] = []

for i in range(case):
    start_node, end_node = map(str, input().split())
    graph[start_node].append(end_node)
    graph[end_node].append(start_node)

result = dfs(graph, "1")
print(len(result)-1)


