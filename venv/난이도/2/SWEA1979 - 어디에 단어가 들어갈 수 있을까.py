'''
SWEA1979 - 어디에 단어가 들어갈 수 있을까 (D2)
'''

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = []
    ans = 0
    for n in range(N):
        puzzle.append(list(map(int, input().split())))

    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count += 1
                if j == N-1 and count == K:
                    ans += 1
            else:
                if count == K:
                    ans += 1
                count = 0


    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                count += 1
                if j == N-1 and count == K:
                    ans += 1
            else:
                if count == K:
                    ans += 1
                count = 0
    print('#{} {}'.format(t, ans))











