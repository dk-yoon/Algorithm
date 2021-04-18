T = int(input())
dr = [-1, -1, -1, 0, 1, 1, 1, 0]
dc = [-1, 0, 1, 1, 1,  0, -1, -1]

for t in range(1, T + 1):
    N, M = map(int, input().split())
    
    arr = [[0] * N for _ in range(N)]
    base = int(N / 2) - 1
    arr[base][base], arr[base + 1][base + 1] = 2, 2
    arr[base][base + 1], arr[base + 1][base] = 1, 1
    for _ in range(M):
        c, r, dol = map(int, input().split())
        c, r = c - 1, r - 1
        arr[r][c] = dol
        for i in range(8):
            nr, nc = r + dr[i], c + dc[i]
            while 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] == 0: break
                if arr[nr][nc] == dol:
                    tr, tc = nr - dr[i], nc - dc[i]
                    while tr != r or tc != c:
                        arr[tr][tc] = dol
                        tr, tc = tr - dr[i], tc - dc[i]
                    break
                nr, nc = nr + dr[i], nc + dc[i]
    w = b = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1: b += 1
            elif arr[i][j] == 2: w += 1

    print('#{} {} {}'.format(t, b, w))