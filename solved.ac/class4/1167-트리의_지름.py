'''
이거 솔직히 방법 봐야됨. 생각못함.

'''
import sys
from collections import deque

case_count = int(input())
tree = [[] for _ in range(case_count + 1)]

for i in range(case_count):
    case = list(map(int, sys.stdin.readline().rstrip().split()))
    for j in range(1, len(case) - 1, 2):
        tree[case[0]].append((case[j], case[j + 1]))

# print(tree)


def bfs(start):
    queue = deque()
    visited = [-1] * (case_count + 1)
    queue.append(start)
    visited[start] = 0
    max_values = [0, 0]

    while queue:
        current = queue.popleft()
        for point, distance in tree[current]:
            if visited[point] == -1:
                queue.append(point)
                visited[point] = visited[current] + distance
                if max_values[0] < visited[point]:
                    max_values = visited[point], point

    return max_values


max_distance_1, point_1 = bfs(1)
max_distance_2, point_2 = bfs(point_1)
print(max_distance_2)
