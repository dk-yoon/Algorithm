'''
BOJ1012 - 유기농배추 (그래프 이론, 그래프 탐색, BFS, DFS)
'''
import sys
sys.setrecursionlimit(10**8)    # 재귀 상환값을 default보다 높게 설정

def possible(y,x):  # 이동 가능한 조건
    return 0 <= y < N and 0 <= x < M

def DFS(now_y, now_x):
    global count
    farm[now_y][now_x] = 0  # 한번 탐색한 영역을 0으로 변경하여 추후 탐색 안하도록 설정
    count += 1

    for i in range(4):  # 상하좌우 탐색 진행
        move_y = now_y + dy[i]
        move_x = now_x + dx[i]
        if possible(move_y, move_x) and farm[move_y][move_x] == 1:  # 이동 가능하며 상하좌우에 배추가 있을 때
            DFS(move_y, move_x) # 이동 후 추가 탐색 진행


T = int(input())
dy = [-1, 1, 0, 0]  # 방향 탐색을 위한 델타 활용
dx = [0, 0, -1, 1]

for t in range (T):
    M, N, num_cabbage = map(int, input().split())
    farm  = [[0] * M for _ in range(N)]
    ans = []
    count = 0

    for _ in range(num_cabbage):
        x, y = map(int, input().split())    # 배추가 있는 영역의 데이터를 1로 변경
        farm[y][x] = 1


    for y in range(N):
        for x in range(M):
            if farm[y][x] ==  1:  # 시작 지점의 인덱스를 찾아 출발점으로 설정
                count = 0
                DFS(y, x)   # 배추가 있는 지점부터 탐색을 시작
                ans.append(count)

    print(len(ans)) # 최종 지렁이가 필요한 영역의 수 출력
