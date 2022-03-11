import math

N = int(input())
cnt = 0

number = str(math.factorial(N))
reversed_number = number[::-1]
for char in reversed_number:
    if char == '0':
        cnt += 1
    else:
        break
print(cnt)
