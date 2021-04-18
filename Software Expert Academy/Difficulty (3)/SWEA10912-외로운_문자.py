T = int(input())
for t in range(1, T + 1):
    word = list(input())
    count = [0] * 26
    answer = []
    for alphabet in word:
            count[ord(alphabet) - 97] += 1
    for i in range(len(count)):
        if count[i] % 2:
            answer.append(chr(i + 97))
    if len(answer) == 0:
        print('#{0} Good'.format(t))
    else:
        print('#{0} {1}'.format(t, ''.join(answer)))
