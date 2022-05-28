from itertools import combinations

n, s = map(int, input().split())

numbers = list(map(int, input().split()))
temp = []
cnt = 0

for i in range(1, len(numbers) +1):
    temp.extend(list(combinations(numbers, i)))

for value in temp:
    if sum(value) == s:
        cnt +=1

print(cnt)


