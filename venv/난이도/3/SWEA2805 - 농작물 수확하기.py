'''
SWEA2805 - 농작물 수확하기 (D3)
'''
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    farm = []
    sum_list = []
    for _ in range(N):
        farm.append(list((input())))
    center = int((N + 1) / 2)-1
    move = center
    for i in range(N):
        for j in range(abs(center - i), (N - move)):
            sum_list.append(int(farm[i][j]))
        if i < center:
            move -= 1
        else:
            move += 1
    print('#{} {}'.format(t, sum(sum_list)))
