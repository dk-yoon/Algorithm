'''
SWEA4866 - 괄호검사 (D2)
'''

T = int(input())
for t in range(1, T + 1):
    input_list = list(input())
    stack = []
    flag = True
    for input_word in input_list:
        if input_word == '(' or input_word == '{':
            stack.append(input_word)

        elif input_word == ')':
            if len(stack) == 0:
                flag = False
                break
            pop_value = stack.pop()
            if pop_value != '(':
                flag = False

        elif input_word == '}':
            if len(stack) == 0:
                flag = False
                break
            pop_value = stack.pop()
            if pop_value != '{':
                flag = False

    if len(stack) > 0:
        flag = False

    print('#{} {}'.format(t, int(flag)))