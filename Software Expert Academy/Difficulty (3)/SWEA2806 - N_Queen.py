'''
SWEA2806 - N Queen (D3)
'''
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    visit = [0] * N
    cols = [0] * N

    def promising(k, c):
        for i in range(k):
            if k - i == abs(c - cols[i]):
                return False
        return True

    def nQueen(k):
        global ans
        if k == N:
            ans += 1
        else:
            for i in range(N):
                if visit[i] or not promising(k, i):
                    continue
                visit[i] = 1
                cols[k] = i
                nQueen(k + 1)
                visit[i] = 0

    ans = 0
    nQueen(0)
    print(f'#{t} {ans}')