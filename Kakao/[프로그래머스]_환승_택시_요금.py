import heapq


def solution(n, s, a, b, fares):
    graph = {}

    for fare in fares:
        if fare[0] not in graph:
            graph[fare[0]] = {fare[1]: fare[2]}
        else:
            graph[fare[0]][fare[1]] = fare[2]

        if fare[1] not in graph:
            graph[fare[1]] = {fare[0]: fare[2]}
        else:
            graph[fare[1]][fare[0]] = fare[2]

    # print(graph)
    answer = 1000000000

    distances = dijk(graph, s)
    # print(distances)
    for key, value in distances.items():
        # print(key, value)
        a_distances = dijk(graph, key)
        b_distances = dijk(graph, key)
        # print(key, value, a_distances[a])
        # print(key, value, b_distances[b])
        # print("distances: ", a_distances[a], b_distances[b], value)
        distance = value + a_distances[a] + b_distances[b]
        # print(distance)
        answer = min(answer, distance)
    # print(distances)
    return answer


def dijk(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # 시작 값은 0이어야 함
    queue = []
    heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while queue:  # queue에 남아 있는 노드가 없으면 끝
        current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

        if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
            if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

    return distances
