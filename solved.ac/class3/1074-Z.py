"""
그냥 재귀로 했을 시에는 시간초과 문제 발생

n, r, c = map(int, input().split())

cnt = 0

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]


def make_map(n, row, col):
    global cnt
    if n == 2:
        for i in range(4):
            x = row + dx[i]
            y = col + dy[i]
            if x == r and y == c:
                print(cnt)
                exit()
            cnt += 1
    else:
        make_map(n // 2, row, col)
        make_map(n // 2, row, col + n // 2)
        make_map(n // 2, row + n // 2, col)
        make_map(n // 2, row + n // 2, col + n // 2)


make_map(2**n, 0, 0)
"""
n, r, c = map(int, input().split())
cnt = 0

dr = [0, 0, 1, 1]
dc = [0, 1, 0, 1]


def make_map(n, r, c):
    global cnt
    while n > 1:
        row = 2 ** n
        flag = row // 2

        if r < flag and c < flag:
            pass
        elif r < flag and c >= flag:
            cnt += flag ** 2
            c -= flag
        elif r >= flag and c < flag:
            cnt += flag ** 2 * 2
            r -= flag
        else:
            cnt += flag ** 2 * 3
            r -= flag
            c -= flag
        n -= 1
    for i in range(4):
        if r == dr[i] and c == dc[i]:
            print(cnt +i)


make_map(n, r, c)
