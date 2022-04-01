import sys

n = int(input())

student_map = [[0] * n for _ in range(n)]
value_map = [[0] * n for _ in range(n)]
student_table = []
student_table_map = dict()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n*n):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    student_table.append(row)
    student_table_map[row[0]] = row[1:]

def is_out_range(i, j):
    return i>=n or j>=n or i<0 or j<0

def first_condition(student_info):
    first_condition_info = list()
    for i in range(n):
        for j in range(n):
            if student_map[i][j] == 0:
                score=0
                score_2 = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if is_out_range(nx, ny):
                        continue
                    if student_map[nx][ny] in student_info[1:]:
                        score +=1
                    if student_map[nx][ny] == 0:
                        score_2 +=1

                first_condition_info.append([i, j, score, score_2])

    result = sorted(first_condition_info, key=lambda item: (item[2], item[3], -item[0], -item[1]), reverse=True)

    return result


for student_info in student_table:
    first = first_condition(student_info)
    student_map[first[0][0]][first[0][1]] = student_info[0]

# print(student_map)
# print(student_table_map)
result = 0
for i in range(n):
    for j in range(n):
        score = 0
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            if is_out_range(nx, ny):
                continue

            if student_map[nx][ny] in student_table_map[student_map[i][j]]:
                score +=1
        if score == 0:
            result +=0
        elif score == 1:
            result +=1
        elif score ==2:
            result += 10
        elif score ==3:
            result += 100
        elif score == 4:
            result += 1000



print(result)






