import sys

n = int(input())

time_table = []

for i in range(n):
    start_time, end_time = map(int, sys.stdin.readline().rstrip().split())
    time_table.append([start_time, end_time])

# print(time_table)

time_table.sort(key=lambda x: (x[1], x[0]))

cnt = 1
flag = time_table[0][1]
for time in time_table[1:]:
    if flag <= time[0]:
        cnt += 1
        flag = time[1]

print(cnt)
