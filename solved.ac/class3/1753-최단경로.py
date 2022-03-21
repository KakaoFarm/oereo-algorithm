import heapq
import sys

n, m = map(int, input().split())

start_point = int(input())

graph = [[] for _ in range(n+1)]
visited= [False] * (n+1)
distances = [int(1e9)] * (n+1)

# graph setting
for i in range(m):
    start, end, weight = map(int, sys.stdin.readline().rstrip().split())
    graph[start].append((end, weight))

def get_smaller_node():
    smallest_value = int(1e9)
    index = 0

    for i in range(1, n+1):
        if distances[i] < smallest_value and not visited[i]:
            smallest_value = distances[i]
            index = i
    return index

def graph_searching(start):
    queue = []
    heapq.heappush(queue, [0, start])
    distances[start] = 0
    visited[start] = True

    while queue:
        current_weight, current_node = heapq.heappop(queue)
        if distances[current_node]< current_weight:
            continue
        for line in graph[current_node]:
            node = line[0]
            weight = line[1]
            cost = current_weight + weight
            if cost<distances[node]:
                distances[node] = cost
                heapq.heappush(queue, [cost, node])


def main():
    graph_searching(start_point)
    for i in range(1, n+1):
        if distances[i] == int(1e9):
            print("INF")
        else:
            print(distances[i])

main()