'''
BOJ2667 - 단지번호붙이기 (그래프 이론, 그래프 탐색, DFS, BFS)
'''
def possible(y,x):  # 이동 가능한 조건
    return 0 <= y < N and 0 <= x < N

def DFS(now_y, now_x):
    global count
    town[now_y][now_x] = 0
    count += 1

    for i in range(4):  # 상하좌우 탐색 진행
        move_y = now_y + dy[i]
        move_x = now_x + dx[i]
        if possible(move_y, move_x) and int(town[move_y][move_x]) == 1:  # 이동 가능 조건과 탐색 미진행 상태인 경우
            DFS(move_y, move_x) # 이동 후 추가 탐색 진행

N = int(input())
dy = [-1, 1, 0, 0]  # 방향 탐색을 위한 델타 활용
dx = [0, 0, -1, 1]
count = 0
town = []
ans = []

for _ in range(N):
    town.append(list(input()))

for y in range(N):
    for x in range(N):
        if town[y][x] == '1':  # 시작 지점의 인덱스를 찾아 출발점으로 설정
            count = 0
            DFS(y, x)
            ans.append(count)

print(len(ans))
for i in sorted(ans):
    print(i)

