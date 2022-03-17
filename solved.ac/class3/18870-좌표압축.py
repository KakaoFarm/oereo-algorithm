import sys

n = int(input())

points = list(map(int, sys.stdin.readline().rstrip().split()))

# print(points)
sorted_points = sorted(set(points))
# print(sorted_points)
table = {}

for i in range(len(sorted_points)):
    table[sorted_points[i]] = i

for point in points:
    print(table[point], end=" ")
