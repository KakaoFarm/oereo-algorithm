n = int(input())

for i in range(n):
    case = int(input())

    dp = [0] * (101)

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    if case > 5:
        for i in range(6, case + 1):
            dp[i] = dp[i - 1] + dp[i - 5]

    print(dp[case])
