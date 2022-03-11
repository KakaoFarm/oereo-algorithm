import sys

N, target_money = map(int, input().split())

moneys = list()
for i in range(N):
    moneys.append(int(sys.stdin.readline().rstrip()))


moneys.reverse()
cnt = 0

for money in moneys:
    cnt += target_money // money
    target_money %= money

print(cnt)