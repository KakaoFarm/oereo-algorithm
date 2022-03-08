import sys
from collections import deque


def main():
    test_case = int(input())

    for case_count in range(test_case):
        function_command = sys.stdin.readline().rstrip()
        numbers_count = int(sys.stdin.readline())
        queue = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
        if numbers_count == 0:
            queue = deque()

        result_queue = calculate(function_command, queue, numbers_count)

        if result_queue == "error":
            print(result_queue)
        else:
            print("[" + ",".join(result_queue) + "]")


def calculate(function_command, queue, numbers_count):
    is_flip = False
    for command in function_command:
        if command == "R":
            is_flip = not is_flip
        if command == "D":
            if len(queue) !=0:
                if is_flip is True:
                    queue.pop()
                else:
                    queue.popleft()
            else:
                return "error"
    if is_flip is True:
        queue.reverse()
    return queue

main()


