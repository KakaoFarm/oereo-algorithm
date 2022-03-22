equation = input().split('-')

result = 0
first_num = equation[0].split('+')

for i in first_num:
    result += int(i)

for i in equation[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)