n, m = map(int, input().split())

password_map = dict()

for i in range(n):
    site, password = map(str, input().split())
    password_map[site] = password

# print(password_map)

for i in range(m):
    site = str(input())
    print(password_map[site])