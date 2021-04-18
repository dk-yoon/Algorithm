'''
SWEA5105 - 미로의 거리 (D3)
'''

def possible(y,x):  # 이동 가능한 조건
    return 0 <= y < N and 0 <= x < N and (maze[y][x] == 0 or maze[y][x] == 3)

def BFS(now_y, now_x):
    global result

    Q.append((now_y, now_x))
    visit.append((now_y, now_x))    # 탐색한 인덱스 내역 저장

    while Q:
        now_y, now_x = Q.pop(0)
        for i in range(4):  # 상하좌우 탐색 진행
            move_y = now_y + dy[i]
            move_x = now_x + dx[i]
            if possible(move_y, move_x) and (move_y, move_x) not in visit:  # 이동 가능 조건과 탐색 미진행 상태인 경우
                Q.append((move_y, move_x))
                visit.append((move_y, move_x))
                Distance[move_y][move_x] = Distance[now_y][now_x] + 1

                if maze[move_y][move_x] == 3:  # 도착지점에 와있는 경우, 전역변수 result 변경 후 함수 종료
                    result = Distance[move_y][move_x] - 1
                    return

T = int(input())

for t in range(1, T+1):
    N = int(input())
    dy = [-1, 1, 0, 0]  # 방향 탐색을 위한 델타 활용
    dx = [0, 0, -1, 1]
    Q = []
    maze = []

    for _ in range(N):
        maze.append(list(map(int, input())))

    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2: # 시작 지점의 인덱스를 찾아 출발점으로 설정
                now_y, now_x = y, x

    visit = []
    Distance = [[0] * N for _ in range(N)]
    result = 0
    BFS(now_y, now_x)

    print('#{} {}'.format(t, result))