'''
BOJ5427 - 불 (그래프 이론, 그래프 탐색, BFS)
'''
from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    cnt = 0  # 시간 체크

    while True:

        if len(q) == 0: # 탐색을 다 마쳤는지
            break

        while fire: # 불 먼저 이동
            if fire[0][2] == cnt:  # 진행시간까지만 불이 퍼지도록, 이후로도 퍼지면 결과에 영향
                break
            y, x, time = fire.popleft() # 좌표와 탐색 당시 시간이 담김
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= ny < Y and 0 <= nx < X: # 빌딩 내부 탐색
                    if building[ny][nx] == "." or building[ny][nx] == "@":  # 사람이 있거나 있던 자리나 빈자리만 불이 번짐
                        building[ny][nx] = "*"
                        fire.append((ny, nx, time + 1)) # 다음번 탐색지점과 당시 시간 추가

        while q:   # 불 번진 이후 사람 이동
            if q[0][2] == cnt:  # 진행시간까지만 사람 이동
                break
            y, x, time = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= ny < Y and 0 <= nx < X:
                    if building[ny][nx] == "." and not visit[ny][nx]:   # 아직 방문하지 않은 빈공간 탐색
                        visit[ny][nx] = 1
                        q.append((ny, nx, time + 1))
                else:
                    return cnt

        cnt += 1  # 시간이 1씩 증가
    return 'IMPOSSIBLE'



T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    q = deque()  # 인간 큐
    fire = deque()  # 불 큐
    building = []
    visit = [[0] * X for x in range(Y)]

    for y in range(Y):
        building.append(list(input()))

    for y in range(Y):
        for x in range(X):
            if building[y][x] == "@":
                q.append((y, x, 0))
            elif building[y][x] == "*":
                fire.append((y, x, 0))

    print(bfs())
