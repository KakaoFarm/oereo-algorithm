import sys

N = int(input())
pool = set()


def is_number_in_pool(num):
    if num in pool:
        return True
    return False


for i in range(N):
    command = sys.stdin.readline().rstrip().split()

    if len(command) == 1:
        if command[0] == "all":
            pool = set([i for i in range(1, 21)])
        elif command[0] == "empty":
            pool = set()
        continue

    if command[0] == "add":
        pool.add(int(command[1]))
    elif command[0] == "remove":
        pool.discard(int(command[1]))

    elif command[0] == "check":
        if is_number_in_pool(int(command[1])):
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        if is_number_in_pool(int(command[1])):
            pool.discard(int(command[1]))

        else:
            pool.add(int(command[1]))

