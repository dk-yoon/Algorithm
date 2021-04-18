'''
SWEA1859 - 백만장자 프로젝트 (D2)
'''
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    sell_list = (list(map(int, input().split())))
    total = 0
    max_value = sell_list[-1]

    for i in range(len(sell_list)-1,-1,-1):
        if sell_list[i] < max_value:
            total += max_value - sell_list[i]
        elif sell_list[i] > max_value:
            max_value = sell_list[i]
    print('#{} {}'.format(t, total))
