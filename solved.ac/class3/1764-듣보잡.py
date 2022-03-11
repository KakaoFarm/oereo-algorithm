import sys

N, M = map(int, input().split())

no_hear_peoples = list()
no_see_peoples = list()

for i in range(N):
    name = sys.stdin.readline().rstrip()
    no_hear_peoples.append(name)

for i in range(M):
    name = sys.stdin.readline().rstrip()
    no_see_peoples.append(name)

result = list(set(no_hear_peoples) & set(no_see_peoples))
result.sort()
print(len(result))

for name in result:
    print(name)