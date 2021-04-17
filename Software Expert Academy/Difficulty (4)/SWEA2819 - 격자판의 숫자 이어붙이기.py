'''
SWEA2819 - 격자판의 숫자 이어붙이기 (D4)
'''
def DFS(y, x, cnt, string):
    if cnt == 7:
        ans.append(string)
        return

    else:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 4 and 0 <= nx < 4:
                DFS(ny, nx, cnt + 1, string + arr[ny][nx])

dx = [0,0,-1,1]
dy = [-1,1,0,0]

T = int(input())
for t in range(1, T + 1):
    arr = []
    for _ in range(4):
        arr.append(input().split())

    ans = []

    for y in range(4):
        for x in range(4):
            DFS(y, x, 1, arr[y][x])

    print(f'#{t} {(len(set(ans)))}')