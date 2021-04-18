'''
SWEA1226 - 미로 (D4)
'''
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def BFS(r, c):
    Q = [(r,c)]

    while Q:
        cur_r, cur_c = Q.pop(0)

        for i in range(4):
            nr = cur_r + dr[i]
            nc = cur_c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc > N:
                continue

            if maze[nr][nc] == 3:
                return 1

            if maze[nr][nc] != 1:
                Q.append((nr,nc))
                maze[nr][nc] = 1
    return  0

# def DFS(r, c):
#     global flag
#
#     if maze[r][c] == 3:
#         flag = 1
#         return
#
#     maze[r][c] = 1
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#
#         if nr < 0 or nr >= N or nc < 0 or nc > N:
#             continue
#
#     if maze[nr][nc] != 1:
#         DFS[nr][nc]

for t in range(10):
    tc_num = int(input())
    N = 100

    maze = [list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sR = i
                sC = j
                maze[i][j] = 1
    print('#{} {}'.format(tc_num, BFS(sR, sC)))