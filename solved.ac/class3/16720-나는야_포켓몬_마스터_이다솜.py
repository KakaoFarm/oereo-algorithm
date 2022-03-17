import sys

n, m  = map(int, input().split())

pocket_mon_dictionary = {}
for i in range(n):
    pocket_mon = sys.stdin.readline().rstrip()
    pocket_mon_dictionary[pocket_mon] = str(i+1)
    pocket_mon_dictionary[str(i+1)] = pocket_mon

for i in range(m):
    searched_pocket_mon = sys.stdin.readline().rstrip()
    print(pocket_mon_dictionary[searched_pocket_mon])

# print(pocket_mon_dictionary)