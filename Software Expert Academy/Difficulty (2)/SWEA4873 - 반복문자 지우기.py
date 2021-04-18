'''
SWEA4873 - 반복문자 지우기 (D2)
'''

T = int(input())
for t in range(1, T + 1):
    letters = input()
    stack = []

    for letter in letters:
        if len(stack) == 0:
            stack.append(letter)
        else:
            if stack[len(stack) - 1] == letter:
                stack.pop()
            else:
                stack.append(letter)
    print('#{} {}'.format(t, len(stack)))
