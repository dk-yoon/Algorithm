'''
BOJ7576 - 토마토 (그래프 이론, 그래프 탐색, BFS)
'''
from collections import deque

def possible(x,y):
        return 0 <= x < N and 0 <= y < M    # 리스트 벗어나는 탐색을 방지

def BFS():
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            # 큐마다 안해주면 전체 0만큼 카운트가 오름 (while문 계속 반복해서 cnt 증가)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if possible(nx, ny) and box[nx][ny] == 0:
                    box[nx][ny] += 1
                    queue.append((nx, ny))  # 신규 탐색 영역을 큐에 추가

    for column in box:
        if 0 in column:
            return -1 # BFS 순회 후에도 모두 익지 않았을 때
    return cnt - 1  # 마지막 큐 탐색하면서 오른거 다시 차감

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
M, N = map(int, input().split())
box = []
queue = deque()

for n in range(N):
    box.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:  # 토마토가 익은 곳을 BFS 탐색 대상으로 추가
            queue.append((i, j))

print(BFS())