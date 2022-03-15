import sys
from collections import deque

n = int(input())

for i in range(n):
    case_len, important = map(int, input().split())

    queue_idx = deque()
    cases = list(map(int, sys.stdin.readline().rstrip().split()))
    queue = deque(cases)
    for j in range(len(cases)):
        # queue.append(cases[j])
        queue_idx.append(j)
    cnt = 0

    while True:
        max_num = max(queue)
        value = queue.popleft()
        index = queue_idx.popleft()
        if max_num == value:
            if index == important:
                break
            else:
                cnt +=1

        else:
            queue.append(value)
            queue_idx.append(index)
    print(cnt+1)