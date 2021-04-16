'''
SWEA4366 - 정식이의 은행업무 (D4)
'''
T = int(input())
for t in range(1, T + 1):
    bin_num = input()
    ter_num_origin = input()
    bin_len = len(bin_num)
    ter_len = len(ter_num_origin)
    bin_num = int(bin_num, 2)
    ter_num = int(ter_num_origin, 3)
    bin_list = []
    ter_list = []

    for i in range(bin_len):
        bin_list.append(bin_num ^ (1 << i))

    for j in range(ter_len):
        if ter_num_origin[j] == '0':
            ter_list.append(ter_num + (3 ** (ter_len - 1 - j)))
            ter_list.append(ter_num + 2 * (3 ** (ter_len - 1 - j)))
        elif ter_num_origin[j] == '1':
            ter_list.append(ter_num - (3 ** (ter_len - 1 - j)))
            ter_list.append(ter_num + (3 ** (ter_len - 1 - j)))
        else:
            ter_list.append(ter_num - (3 ** (ter_len - 1 - j)))
            ter_list.append(ter_num - 2 * (3 ** (ter_len - 1 - j)))

    for num in bin_list:
        if num in ter_list:
            print(f'#{t} {num}')
