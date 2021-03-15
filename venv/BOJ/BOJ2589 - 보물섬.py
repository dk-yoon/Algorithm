'''
BOJ2589 - 보물섬 (그래프 이론, 그래프 탐색, 브루트포스 알고리즘, BFS)
'''
from collections import deque

def bfs(y,x):
    global distance
    distance = 0
    cnt = 0
    q = deque()
    q.append((y, x, cnt))  # 시작 노드를 큐에 넣어줌
    visit[y][x] = 1

    while q:
        y, x, cnt = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= width or ny >= height:
                continue
            if arr[ny][nx] == 'L' and visit[ny][nx] == 0:
                q.append((ny, nx, cnt + 1))
                visit[ny][nx] = 1
                distance = cnt + 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
height, width = map(int, input().split())
arr = []
for h in range(height):
    arr.append(list(input()))

max_len = -1

for y in range(height):
    for x in range(width):
        if arr[y][x] == 'L':
            visit = [[0] * width for _ in range(height)]
            bfs(y, x)
            if distance > max_len:
                max_len = distance
print(max_len)