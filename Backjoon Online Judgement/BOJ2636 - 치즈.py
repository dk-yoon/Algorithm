'''
BOJ2636 - 치즈 (구현, 그래프 이론, 그래프 탐색, BFS, 시뮬레이션)
'''
from collections import deque

def possible(y,x):
    return 0 <= y < Y and 0 <= x < X    # 이동 가능 범위 계산

def bfs(y,x):
    visit = [[0] * X for _ in range(Y)] # 방문 여부 기록
    q = deque()
    q.append((y,x))
    visit[y][x] = 1
    cnt = 0

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if possible(ny,nx) and visit[ny][nx] == 0:
                if grid[ny][nx] == 0:   # 0일 때 : 겉부분일 때
                    q.append((ny,nx))
                    visit[ny][nx] = 1   # 탐색만 이어나가고 데이터 변경은 일어나지 않음
                    
                elif grid[ny][nx] == 1: # 1일 때 : 공기와 접촉하는 치즈 부분일 때
                    grid[ny][nx] = 0    # 겉부분으로 변화하며 그 갯수를 카운트
                    cnt += 1
                    visit[ny][nx] = 1
    ans.append(cnt) # 시간이 지날 때마다 겉부분 갯수를 기록

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
Y, X = map(int, input().split())
grid = []
visit = [[0] * X for _ in range(Y)]
ans = []

for y in range(Y):
    grid.append(list(map(int, input().split())))

while True:
    bfs(0,0)    # 무조건 공기부분임을 문제에서 명시
    if ans[-1] == 0:    # 더 이상 녹일 치즈가 없는 상황
        break
print(len(ans)-1)   # 0일 때 한번 더 돌리고 break 됐으므로 -1
print(ans[-2])  # 인덱스 -1은 0에 해당하므로 그 이전의 치즈 갯수를 출력