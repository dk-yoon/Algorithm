'''
SWEA1223 - 계산기2 (D4)
'''

T = 10

for t in range(1, T + 1):
    len_origin = int(input())
    origin = input()
    stack = []
    modified = []
    answer = []

    for token in origin:
        if token == '*':
            while stack and stack[len(stack)-1] == '*':
                modified.append(stack.pop())
            stack.append(token)
        elif token == '+':
            while stack and (stack[len(stack) - 1] == '*' or stack[len(stack) - 1] == '+'):
                modified.append(stack.pop())
            stack.append(token)
        else:
            modified.append(token)
    while stack:
        modified.append(stack.pop())

    for i in modified:
        if i == '+':
            num1 = answer.pop()
            num2 = answer.pop()
            answer.append(int(num1) + int(num2))
        elif i == '*':
            num1 = answer.pop()
            num2 = answer.pop()
            answer.append(int(num1) * int(num2))
        else:
            answer.append(i)
    print('#{} {}'.format(t, *answer))