import sys
from collections import deque

n, m = map(int, input().split())

snakes = []
ladders = []
board = [0] * 101

for i in range(n):
    ladder_info = list(map(int, sys.stdin.readline().rstrip().split()))
    ladders.append(ladder_info)

for i in range(m):
    snake_info = list(map(int, sys.stdin.readline().rstrip().split()))
    snakes.append(snake_info)

# print(ladders)
# print(snakes)

position = 0
cnt = 0

# queue = deque([1])
# queue.append([1])

ladder_starts = [i[0] for i in ladders]
snake_starts = [i[0] for i in snakes]

# queue = deque([1])

def game_start():
    queue = deque([1])

    while queue:
        position = queue.popleft()
        for i in range(1, 7):
            n_position = position + i
            # print(n_position)
            if n_position <= 0 or n_position > 100 or board[n_position] != 0:
                continue

            if n_position in ladder_starts:
                index = ladder_starts.index(n_position)
                n_position = ladders[index][1]
            if n_position in snake_starts:
                index = snake_starts.index(n_position)
                n_position = snakes[index][1]
            # print(n_position)
            if board[n_position] == 0:
                queue.append(n_position)
                board[n_position] = board[position] + 1

game_start()
print(board[100])
