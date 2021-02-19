'''
SWEA5356 - 의석이의 세로로 말해요
'''
T = int(input())
for t in range(1, T + 1):
    word_list = []
    ver_list = list([] for _ in range(15))
    answer = []

    for i in range(5):
        word_list.append(list(input()))

    for i in range(5):
        for j in range(len(word_list[i])):
            ver_list[j].append(word_list[i][j])

    for ver_lst in ver_list:
        for ver in ver_lst:
            answer.append(ver)
    print('#{} {}'.format(t, "".join(answer)))