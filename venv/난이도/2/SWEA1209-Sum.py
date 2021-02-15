'''
SWEA1209-Sum
'''

T = 10
for t in range(1, T + 1):
    _ = int(input())
    max_sum = -1
    t_list = []
    for i in range(100):
        t_list.append(list(map(int, input().split())))
    for i in range(100):
        x_sum = 0
        for j in range(100):
            #  행 덧셈
            x_sum += t_list[i][j]
            if x_sum > max_sum:
                max_sum = x_sum

    for j in range(100):
        y_sum = 0
        for i in range(100):
            y_sum += t_list[i][j]
            if y_sum > max_sum:
                max_sum = y_sum

    cross_sum = 0
    for i in range(100):
        cross_sum += t_list[i][i]
        if cross_sum > max_sum:
            max_sum = cross_sum

    cross_sum2 = 0
    for i in range(99, -1, -1):
        cross_sum2 += t_list[i][99-i]
        if cross_sum > max_sum:
            max_sum = cross_sum
    print(f'#{t} {max_sum}')


'''
4 4 3 2 1
2 2 1 6 5
3 5 4 6 7
4 2 5 9 7
8 1 9 5 6
'''
# 5 0
# 4 1
# 3 2
# 2 3
# 1 4