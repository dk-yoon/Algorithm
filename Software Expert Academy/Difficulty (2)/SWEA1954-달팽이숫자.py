'''
SWEA1954 - 달팽이숫자
'''
T = int(input())
for t in range(T):
    N = int(input())
    total = [[0] * N for _ in range(N)]
    for k in range(1, N * N):
        for i in range(N):
            for j in range(N):
                total[i][j] += k
    print(total)