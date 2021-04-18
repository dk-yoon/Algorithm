'''
BOJ10026 - 적록색약 (그래프 이론, 그래프 탐색, DFS. BFS)
'''
import copy
import sys
sys.setrecursionlimit(10**8)

def possible(y,x):  # 이동 가능한 조건
    return 0 <= y < N and 0 <= x < N

def normal(now_y, now_x):
    global count
    color = img[now_y][now_x]
    img[now_y][now_x] = 0
    count += 1

    for i in range(4):  # 상하좌우 탐색 진행
        move_y = now_y + dy[i]
        move_x = now_x + dx[i]
        if possible(move_y, move_x) and img[move_y][move_x] == color:  # 이동 가능 조건과 탐색 미진행 상태인 경우
            normal(move_y, move_x) # 이동 후 추가 탐색 진행

def abnormal(now_y, now_x):
    global count
    color = img2[now_y][now_x]
    img2[now_y][now_x] = 0
    count += 1

    for i in range(4):  # 상하좌우 탐색 진행
        move_y = now_y + dy[i]
        move_x = now_x + dx[i]
        if possible(move_y, move_x) and color in ['G', 'R'] and img2[move_y][move_x] in ['G', 'R']:  # 이동 가능 조건과 탐색 미진행 상태인 경우
            abnormal(move_y, move_x) # 이동 후 추가 탐색 진행
        elif possible(move_y, move_x) and color == 'B' and img2[move_y][move_x] == 'B':  # 이동 가능 조건과 탐색 미진행 상태인 경우
            abnormal(move_y, move_x) # 이동 후 추가 탐색 진행


N = int(input())
dy = [-1, 1, 0, 0]  # 방향 탐색을 위한 델타 활용
dx = [0, 0, -1, 1]
img = []
normal_lst = []
abnormal_lst = []

for n in range(N):
    img.append(list(input()))
img2 = copy.deepcopy(img)

for y in range(N):
    for x in range(N):
        if img[y][x] in ['R', 'B', 'G']:  # 시작 지점의 인덱스를 찾아 출발점으로 설정
            count = 0
            normal(y, x)
            normal_lst.append(count)

print(len(normal_lst), end=" ")

for y in range(N):
    for x in range(N):
        if img2[y][x] in ['R', 'B', 'G']:  # 시작 지점의 인덱스를 찾아 출발점으로 설정
            count = 0
            abnormal(y, x)
            abnormal_lst.append(count)
print(len(abnormal_lst))