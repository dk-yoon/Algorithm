'''
SWEA4874 - Forth (D2)
'''

T = int(input())
for t in range(1, T + 1):
    lst = list(map(str, input().split()))
    S = []
    for element in lst:
        if element == '+':
            if len(S) > 1:
                last = int(S.pop())
                before_last = int(S.pop())
                S.append(last + before_last)
            else:
                print('#{} error'.format(t))
                break

        elif element == '*':
            if len(S) > 1:
                last = int(S.pop())
                before_last = int(S.pop())
                S.append(last * before_last)
            else:
                print('#{} error'.format(t))
                break

        elif element == '-':
            if len(S) > 1:
                last = int(S.pop())
                before_last = int(S.pop())
                S.append(before_last - last)
            else:
                print('#{} error'.format(t))
                break

        elif element == '/':
            if len(S) > 1:
                last = int(S.pop())
                before_last = int(S.pop())
                S.append(before_last // last)
            else:
                print('#{} error'.format(t))
                break

        elif element == '.':
            if len(S) == 1:
                print('#{} {}'.format(t, S[0]))
            else:
                print('#{} error'.format(t))
            break

        else:
            S.append(int(element))
