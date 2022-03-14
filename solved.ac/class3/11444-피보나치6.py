"""
골드2
기본 재귀나 DP 등으로 풀면 시간초과 100%
분할정복으로 풀기
0  1  2  3  4  5  6  7   8   9   10  11  12   13   14   15   16   17
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
         1  1  2  3  6   10  17  26  44  72   116

55 = 2^5 + 23
34 = 2^5 +2
21 = 2^4 + 5

13 = 8 + 5
13 = 2^3 + 2 + (2+1)


8 = 3+5     2^1 + 2^1 +1 + 2^1 + 1
5 = 2 + (2+1)  -> 2^1 + 2^1 +1
3 = 1 + 2   -> 2^1 +1

1 2  1 2  5 4      index 2+3 = 5
2 1  2 1  4 5

1 2 2 3  8 7       index (2 + 3 + 3 + 4) /2 = 6
2 1 3 2  7 8

2 3 2 3  13 12     index 3 + 4 = 7
3 2 3 2  12 13

2 3 3 5  21 19     index (3 + 4 + 4 + 5) / 2  = 8
3 2 5 3  19 21

3 5  3 5  34 30    index 4+5 = 9
5 3  5 3  30 34
"""
from collections import deque

N = int(input())


def divide(num):
    queue = deque()
    result = []
    if num > 4:
        if num % 2 == 0:
            queue.append(((num / 2 - 1), (num / 2)))
            queue.append(((num / 2), (num / 2 + 1)))
        else:
            queue.append(((num // 2), (num // 2 + 1)))
            queue.append(((num // 2), (num // 2 + 1)))

    while queue:
        left, right = queue.popleft()
        if left <= 4:
            result.append(left)
        if right <= 4:
            result.append(right)

        if left > 4:
            if left % 2 == 0:
                queue.append(((left / 2 - 1), (left / 2)))
                queue.append(((left / 2), (left / 2 + 1)))
            else:
                queue.append(((left // 2), (left // 2 + 1)))
                queue.append(((left // 2), (left // 2 + 1)))
        if right > 4:
            if right % 2 == 0:
                queue.append(((right / 2 - 1), (right / 2)))
                queue.append(((right / 2), (right / 2 + 1)))
            else:
                queue.append(((right // 2), (right // 2 + 1)))
                queue.append(((right // 2), (right // 2 + 1)))

    return result


def mul_matrix(matrix_1, matrix_2):
    result_matrix = [[0] * len(matrix_2[0]) for _ in range(2)]
    for k in range(2):
        for i in range(len(matrix_2[0])):
            temp = 0
            for j in range(2):
                temp += matrix_1[k][j] * matrix_2[j][i]
                result_matrix[k][i] = temp % 1000000007
    return result_matrix


def power(adj, n):
    if n == 1:
        return adj
    elif n % 2:
        return mul_matrix(power(adj, n - 1), adj)
    else:
        return power(mul_matrix(adj, adj), n // 2)


# results = divide(N)
# print(results)

# matrix_list = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(len(results) // 2)]

# for i in range(1, len(results), 2):
#     # print("result: ", results[i-1]-1, results[i]-1)
#     matrix_list[i // 2][0][0] = int(results[i - 1] - 1)
#     matrix_list[i // 2][1][1] = int(results[i - 1] - 1)
#     matrix_list[i // 2][0][1] = int(results[i] - 1)
#     matrix_list[i // 2][1][0] = int(results[i] - 1)
    # print(matrix_list)

# result = 0
# print("matrix_list: ", matrix_list)

unit_matrix = [[1, 1], [1, 0]]
# for matrix in matrix_list:
#     result = mul_matrix(unit_matrix, matrix)
#     # print(result)
#     unit_matrix = result

if N < 3:
    if N == 0:
        print(0)
    else:
        print(1)
else:
    result = mul_matrix(power(unit_matrix, N - 2), [[1], [1]])
    print(result[0][0])
