import heapq
import sys

n = int(input())
result = []

for i in range(n):
    case = int(sys.stdin.readline().rstrip())

    if case != 0:
        heapq.heappush(result, (-case, case))

    if case == 0:
        if len(result) == 0:
            print(0)
        else:
            max_num = heapq.heappop(result)[1]
            print(max_num)
