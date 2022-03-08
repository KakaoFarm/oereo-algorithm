'''
시간 초과 케이스
'''

# from queue import PriorityQueue
# import heapq
#
# test_case = int(input())
#
# for case_count in range(test_case):
#     cases = list()
#     command_count = int(input())
#     for command_count in range(command_count):
#         command, value = map(str, input().split())
#         if command == 'I':
#             heapq.heappush(cases, int(value))
#         elif command == 'D':
#             if len(cases) == 0:
#                 continue
#             else:
#                 if int(value) == 1:
#                     cases.pop(cases.index(heapq.nlargest(len(cases), cases)[0]))
#                 if int(value) == -1:
#                     heapq.heappop(cases)
#         # print("step",command, value ,"list", cases)
#
#     if len(cases) == 0:
#         print("EMPTY")
#     else:
#         print(cases[len(cases)-1], cases[0])

import sys;
import heapq

result = []
test_case = int(sys.stdin.readline())

for T in range(test_case):
    visited = [False] * 1_000_001
    min_heap = []
    max_heap = []

    command_count = int(sys.stdin.readline())

    for i in range(command_count):
        command = sys.stdin.readline().split()
        if command[0] == 'I':
            heapq.heappush(min_heap, (int(command[1]), i))
            heapq.heappush(max_heap, (-int(command[1]), i))
            visited[i] = True
        elif command[1] == '1':
            while max_heap and not visited[max_heap[0][1]]:
                # print("step1_max: ", max_heap)
                # print("step1_max: ", visited)
                heapq.heappop(max_heap)
            if max_heap:
                # print("step2_max: ", max_heap)
                # print("step2_max: ", visited)
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        else:
            while min_heap and not visited[min_heap[0][1]]:
                # print("step1_min: ", min_heap)
                # print("step1_min: ", visited)
                heapq.heappop(min_heap)
            if min_heap:
                # print("step2_min: ", min_heap)
                # print("step2_min: ", visited)
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)

    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    result.append(f'{-max_heap[0][0]} {min_heap[0][0]}' if max_heap and min_heap else 'EMPTY')

print('\n'.join(result))
