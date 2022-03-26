import heapq
import sys

n = int(input())
m = int(input())

table = [[] for _ in range(n+1)]
# for i in range(n + 1):
#     table[i] = {}

for i in range(m):
    bus_info = list(map(int, sys.stdin.readline().rstrip().split()))
    table[bus_info[0]].append((bus_info[1], bus_info[2]))

start, end = map(int, sys.stdin.readline().rstrip().split())
# print(table)

visited = [0] * (n + 1)


def print_result( fairs):
    print(fairs[end])
    # print(fairs)


def trace(start, end, visited, fairs):
    # print(visited)
    res = [end]
    visited[start] = 0
    while visited[end]:
        res.append(visited[int(end)])
        end = visited[int(end)]
    return print_result(fairs)


def dijkstra(table, start, end):
    fairs = [float('inf') for _ in range(n+1)]
    fairs[start] = 0
    queue = []

    heapq.heappush(queue, [fairs[start], start])

    while queue:
        current_fair, current_destination = heapq.heappop(queue)

        if fairs[current_destination] < current_fair:
            continue
        for new_destination, new_fair in table[current_destination]:
            # print(new_destination, new_fair)
            fair = current_fair + new_fair
            if fair < fairs[new_destination]:
                fairs[new_destination] = fair
                visited[new_destination] = current_destination
                heapq.heappush(queue, [fair, new_destination])

    return print_result(fairs)


dijkstra(table, start, end)

# print(fairs, visited)
