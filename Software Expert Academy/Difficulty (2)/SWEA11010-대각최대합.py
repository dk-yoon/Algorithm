'''
SWEA11010 - 대각최대합
'''
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    t_list = []
    total = [([0] * N) for _ in range(N)]
    max_sum = 0
    for n in range(N):
        t_list.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            total[i][j] += t_list[i][j]
            for k in range(1, N):
                # 좌측 상단 대각선
                if i - k >= 0 and j - k >= 0:
                    total[i][j] += t_list[i-k][j-k]
                # 좌측 하단 대각선
                if i - k >= 0 and j + k <= N-1:
                    total[i][j] += t_list[i-k][j+k]
                # 우측 상단 대각선
                if i + k <= N-1 and j - k >= 0:
                    total[i][j] += t_list[i+k][j-k]
                # 우측 하단 대각선
                if i + k <= N-1 and j + k <= N-1:
                    total[i][j] += t_list[i+k][j+k]

    for answer in total:
        if max(answer) >= max_sum:
            max_sum = max(answer)
    print(f'#{t} {max_sum}')