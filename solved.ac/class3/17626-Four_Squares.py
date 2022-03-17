"""
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 1
-> 잘 몰라서 참고...
"""

"""
CASE 1 시간 초과 ....
"""
# def is_sqrt_number(number):
#     if number == int(math.sqrt(number)) ** 2:
#         return True
#     return False
#
#
# if is_sqrt_number(N):
#     print(1)
# else:
#     for i in range(2, N + 1):
#         if is_sqrt_number(i):
#             dp[i] = 1
#         else:
#             temp = list()
#             for j in range(1, math.floor(math.sqrt(i)) + 1):
#                 temp.append(dp[i - (j ** 2)] + 1)
#             dp[i] = min(temp)
#
#     print(dp[N])

import sys
import math

N = int(sys.stdin.readline())

dp = [0] * (N + 1)
dp[1] = 1


def is_sqrt_number(number):
    if number == int(math.sqrt(number)) ** 2:
        return True
    return False


if is_sqrt_number(N):
    print(1)

for i in range(2, N + 1):
    minValue = 1e9
    if N > i * i and is_sqrt_number(N - i * i):
        print(2)
    for j in range(1, int(i ** 0.5) + 1):
        minValue = min(minValue, dp[i - j * j] + 1)
        dp[i] = minValue

print(dp[N])
