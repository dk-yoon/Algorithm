'''
SWEA10593 - 가로세로 합
'''
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    t_list = []
    total = [([0] * N) for _ in range(N)]

    for i in range(N):
        t_list.append(list(map(int, input().split())))
        for j in range(N):
            total[i][j] -= t_list[i][j]
            total[i][j] += sum(t_list[i])

    list_v = []
    for j in range(N):
        k = []
        for i in range(N):
            k.append(t_list[i][j])
        list_v.append(k)

    for j in range(N):
        for i in range(N):
            total[i][j] += sum(list_v[j])

    max_value = 0
    for ans in total:
        if max(ans) >= max_value:
            max_value = max(ans)
    print(f'#{t} {max_value}')
