from collections import deque

start, end = map(int, input().split())


def bfs(start, end):
    time = [0] * 100001
    max_time = 100000
    queue = deque()
    queue.append(start)

    while queue:

        point = queue.popleft()
        if point == end:
            break
        else:
            moved_point = point + 1
            if 0 <= moved_point <= max_time and not time[moved_point]:
                queue.append(moved_point)
                time[moved_point] = time[point] + 1

            moved_point = point - 1
            if 0 <= moved_point <= max_time and not time[moved_point]:
                queue.append(moved_point)
                time[moved_point] = time[point] + 1

            moved_point = point * 2
            if 0 <= moved_point <= max_time and not time[moved_point]:
                queue.append(moved_point)
                time[moved_point] = time[point] + 1

    return time[end]


print(bfs(start, end))
