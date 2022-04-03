equation = input()

operator_map = {'(': 3, '*': 1, '/': 1, '+': 2, '-': 2}

number_stack = []
operator_stack = []

for char in equation:
    if char.isalpha():
        number_stack.append(char)
        # print(char)
    else:
        if char == '(':
            operator_stack.append(char)
        elif char == ')':
            while operator_stack and operator_stack[-1] != '(':
                operator = operator_stack.pop()
                number_stack.append(operator)
            operator_stack.pop()
        else:
            while operator_stack and operator_map[char] >= operator_map[operator_stack[-1]]:
                operator = operator_stack.pop()
                number_stack.append(operator)
            operator_stack.append(char)


result = number_stack + list(reversed(operator_stack))
result_equation = ''
for i in result:
    result_equation += i

print(result_equation)
