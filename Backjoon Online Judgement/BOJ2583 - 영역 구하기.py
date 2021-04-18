'''
BOJ2583 - 영역 구하기 (그래프 이론, 그래프 탐색, BFS, DFS)
'''

import sys
sys.setrecursionlimit(10**8)    # 재귀 상환값을 default보다 높게 설정

def possible(y,x):  # 이동 가능한 조건
    return 0 <= y < M and 0 <= x < N

def DFS(y,x):
    global count
    grid[y][x] = 1  # 한번 탐색한 영역을 1로 변경하여 추후 탐색 안하도록 설정
    count += 1

    for i in range(4):  # 상하좌우 탐색 진행
        ny = y + dy[i]
        nx = x + dx[i]
        if possible(ny, nx) and grid[ny][nx] == 0:  # 이동 가능하며 0으로 비어진 영역일 때
            DFS(ny, nx) # 이동 후 추가 탐색 진행



dy = [-1, 1, 0, 0]  # 방향 탐색을 위한 델타 활용
dx = [0, 0, -1, 1]

M, N, K = map(int, input().split())
grid = [[0] * N for _ in range(M)]
ans = []

for k in range(K):
    temp = list(map(int, input().split()))
    for y in range(temp[1],temp[3]):
        for x in range(temp[0],temp[2]):
            if grid[y][x] == 0:
                grid[y][x] = 1  # 직사각형 내부에 해당하는 영역을 1로 칠함


for y in range(M):
    for x in range(N):
        if grid[y][x] == 0:  # 0으로 비어진 출발점들부터 탐색
            count = 0
            DFS(y, x)
            ans.append(count)
ans.sort()

print(len(ans)) # 각 0으로 비워진 영역의 수
print(*ans) # 해당 영역들의 넓이