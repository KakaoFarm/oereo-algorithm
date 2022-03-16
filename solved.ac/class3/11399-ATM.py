n = int(input())

times = list(map(int, input().split()))

times.sort(reverse=True)
result = 0
for i in range(1, n+1):
    result += times[i-1] * i

print(result)