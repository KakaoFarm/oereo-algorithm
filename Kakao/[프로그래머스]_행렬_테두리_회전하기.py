from collections import deque


def solution(rows, columns, queries):
    answer = []
    matrix = [[0] * (columns + 1) for _ in range(rows + 1)]
    cnt = 0
    for row in range(1, rows + 1, 1):
        for col in range(1, columns + 1, 1):
            cnt += 1
            matrix[row][col] = cnt
    # print(matrix)
    copied_matrix = [item[:] for item in matrix]

    for query in queries:
        temp = deque()
        tmp = 1000000001
        # temp = []
        for i in range(query[1], query[3]):
            copied_matrix[query[0]][i + 1] = matrix[query[0]][i]
            tmp = min(matrix[query[0]][i], tmp)
            # temp.append(copied_matrix[query[0]][i])
            # print(matrix[query[0]][i])
        for i in range(query[0], query[2]):
            copied_matrix[i + 1][query[3]] = matrix[i][query[3]]
            tmp = min(matrix[i][query[3]], tmp)

            # temp.append(copied_matrix[i][query[3]])
            # print(matrix[i][query[3]])
        for i in range(query[3], query[1], -1):
            copied_matrix[query[2]][i - 1] = matrix[query[2]][i]
            tmp = min(matrix[query[2]][i], tmp)
            # temp.append(copied_matrix[query[2]][i])
            # print(matrix[query[2]][i])
        for i in range(query[2], query[0], -1):
            copied_matrix[i - 1][query[1]] = matrix[i][query[1]]
            tmp = min(matrix[i][query[1]], tmp)
            # temp.append(copied_matrix[i][query[1]])
            # print(matrix[i][query[1]])
        matrix = [item[:] for item in copied_matrix]

        # print(copied_matrix)
        # print(min(temp))
        answer.append(tmp)

    return answer
