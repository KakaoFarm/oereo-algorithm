from collections import deque

n, m = map(int, input().split())

queue = deque([i+1 for i in range(n)])
result = []

while queue:
    for i in range(m-1):
        value = queue.popleft()
        queue.append(value)
    resultValue = queue.popleft()
    result.append(resultValue)

print("<", end="")
for i in range(len(result)):
    print(result[i], end="")
    if i != len(result) -1:
        print(", ", end="")

print(">", end="")
