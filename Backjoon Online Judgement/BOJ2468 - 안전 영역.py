'''
BOJ2468 - 안전 영역 (그래프 이론, 그래프 탐색, 브루트포스 알고리즘, DFS, BFS)
'''
import sys
import copy
sys.setrecursionlimit(10**8)    # 재귀상환값을 default보다 높게 설정

def possible(y,x):  # 이동 가능한 조건
    return 0 <= y < N and 0 <= x < N

def DFS(now_y, now_x, lst):
    global count
    alt[now_y][now_x] = 0  # 리스트 값 변경하여 추후 탐색 방지
    count += 1

    for i in range(4):  # 상하좌우 탐색 진행
        move_y = now_y + dy[i]
        move_x = now_x + dx[i]

        if possible(move_y, move_x) and lst[move_y][move_x]:  # 이동 가능하고 물에 안잠긴 상태
            DFS(move_y, move_x, lst) # 이동 후 추가 탐색 진행

N = int(input())
altitudes = []
max_height = -1
max_count = -1
for _ in range(N):
    altitudes.append(list(map(int, input().split())))
dy = [-1, 1, 0, 0]  # 방향 탐색을 위한 델타 활용
dx = [0, 0, -1, 1]

for i in range(N):
    for j in range(N):
        if altitudes[j][i] > max_height:
            max_height = altitudes[j][i]    # 최고값을 찾아 해당 값까지만 반복문 실행 (최대 100)

for height in range(1, max_height+1):
    alt = copy.deepcopy(altitudes)  # 높이별 DFS 시행해야하기 때문에 높이 변경마다 리스트를 복제하여 테스트

    for y in range(N):
        for x in range(N):
            if alt[y][x] < height:  # 물에 잠긴 영역을 0으로 처리 (False 구분을 위함)
                alt[y][x] = 0

    ans = []
    for y in range(N):
        for x in range(N):
            if alt[y][x]:   # 잠기지 않은 영역을 찾아 DFS 시행
                count = 0
                DFS(y, x, alt)
                ans.append(count)
    if len(ans) > max_count:  # 각 높이별 탐색마다 최다 안전영역인지 확인
        max_count = len(ans)
print(max_count)