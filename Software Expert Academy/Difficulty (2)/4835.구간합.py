T = int(input())
for t in range (1, T + 1):
    N, M = map(int,input().split())
    max_num = 0
    min_num = 1000001
    numbers = list(map(int,input().split()))

    for i in range(len(numbers)-M+1):
        add_M = sum(numbers[i:i+M])
        if add_M > max_num:
            max_num = add_M
        if add_M < min_num:
            min_num = add_M
    print(f'#{t} {max_num - min_num}')