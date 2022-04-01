import sys

n = int(input())
file_table = dict()

for i in range(n):
    row = list(map(str, sys.stdin.readline().rstrip().split(".")))
    if row[1] in file_table:
        file_table[row[1]] +=1
    else:
        file_table[row[1]] = 1

# print(file_table)
sorted_file_table = sorted(file_table.items(), key=lambda item: item[0])

for index, value in sorted_file_table:
    print(index, end="")
    print(" ", end="")
    print(value)