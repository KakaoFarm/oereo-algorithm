import heapq
import sys

point_count, edge_count = map(int, input().split())

route_map = [[] for i in range(point_count + 1)]
visited = [0] * (point_count + 1)

for i in range(edge_count):
    start, end, distance = map(int, sys.stdin.readline().rstrip().split())
    route_map[start].append((end, distance))
    route_map[end].append((start, distance))

point1, point2 = map(int, input().split())


def dijkstra(table, start, end):
    fairs = [float('inf') for _ in range(point_count + 1)]
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

    return fairs[end]


choice_1 = dijkstra(route_map, 1, point1) + dijkstra(route_map, point1, point2) + dijkstra(route_map, point2,
                                                                                           point_count)
choice_2 = dijkstra(route_map, 1, point2) + dijkstra(route_map, point2, point1) + dijkstra(route_map, point1,
                                                                                           point_count)

if choice_2 >= float('inf') or choice_1 >= float('inf'):
    print("-1")
else:
    print(min(choice_1, choice_2))
