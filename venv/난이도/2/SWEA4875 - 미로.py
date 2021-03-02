'''
SWEA4875 - 미로 (D2)
NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오.
'''

def possible(y,x):  # 이동 가능한 조건
    return 0 <= y < N and 0 <= x < N and (maze[y][x] == '0' or maze[y][x] == '3')

def DFS(now_y, now_x):
    global result

    if maze[now_y][now_x] == '3': # 도착지점에 와있는 경우, 전역변수 result 변경 후 함수 종료
        result = 1
        return result

    visit.append((now_y, now_x))    # 탐색한 인덱스 내역 저장

    for i in range(4):  # 상하좌우 탐색 진행
        move_y = now_y + dy[i]
        move_x = now_x + dx[i]
        if possible(move_y, move_x) and (move_y, move_x) not in visit:  # 이동 가능 조건과 탐색 미진행 상태인 경우
            DFS(move_y, move_x) # 이동 후 추가 탐색 진행

T = int(input())

for t in range(1, T+1):
    N = int(input())
    dy = [-1, 1, 0, 0]  # 방향 탐색을 위한 델타 활용
    dx = [0, 0, -1, 1]
    maze = []

    for _ in range(N):
        maze.append(list(input()))

    for y in range(N):
        for x in range(N):
            if maze[y][x] == '2': # 시작 지점의 인덱스를 찾아 출발점으로 설정
                now_y, now_x = y, x

    visit = []
    result = 0  # 기본 도착 여부값을 0으로 설정
    DFS(now_y, now_x)

    print('#{} {}'.format(t, result))