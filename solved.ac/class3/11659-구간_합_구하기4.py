import sys

N, M = map(int, input().split())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [0] * (len(numbers)+1)
# dp[0] = numbers[0]
for i in range(1, len(numbers)+1):
    dp[i] = dp[i-1] + numbers[i-1]


for i in range(M):
    start, end = map(int, sys.stdin.readline().rstrip().split())
    print(dp[end] - dp[start-1])