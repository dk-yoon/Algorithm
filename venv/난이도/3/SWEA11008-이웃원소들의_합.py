'''
SWEA11008 - 이웃원소들의 합
'''

T = int(input())

A = []
r = 0 # 기준위치
c = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
sum_dxy = 0

for t in range(1, T+1):
    N = int(input())
    max_sum = -1
    max_c = 0
    max_r = 0
    A = []
    for n in range(N):
        A.append(list(map(int, input().split())))
    for r in range(N, -1, -1):
        for c in range(N, -1, -1):
            for i in range(4):
                nx = r + dx[i]
                ny = c + dy[i]
                if 0 <= nx < N and 0 <= ny < N:
                    sum_dxy += (A[nx][ny])
                if sum_dxy >= max_sum:
                    max_r = r
                    max_c = c
                    max_sum = sum_dxy
            sum_dxy = 0
    print(f'#{t} {max_r} {max_c} {max_sum}')
