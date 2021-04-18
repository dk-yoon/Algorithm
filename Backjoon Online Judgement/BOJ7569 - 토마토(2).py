'''
BOJ7579 - 토마토(2) (그래프 이론, 그래프 탐색, BFS)
'''
from collections import deque

def possible(x,y,z):
        return 0 <= x < H and 0 <= y < N and 0 <= z < M   # 리스트 벗어나는 탐색을 방지

def BFS():
    cnt = 0
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y, z = queue.popleft()
            # 큐마다 안해주면 전체 0만큼 카운트가 오름 (while문 반복으로 cnt 증가)
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if possible(nx, ny, nz) and box[nx][ny][nz] == 0: # [H해당][N해당][M해당]
                    box[nx][ny][nz] += 1
                    queue.append((nx, ny, nz))  # 신규 탐색 영역을 큐에 추가

    for lst1 in box:
        for lst2 in lst1:
            if 0 in lst2:
                return -1 # BFS 순회 후에도 모두 익지 않았을 때
    return cnt - 1  # 마지막 큐 탐색하면서 오른거 다시 차감

dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
M, N, H = map(int, input().split())
box = []
queue = deque()

for h in range(H):
        box.append([list(map(int, input().split())) for n in range(N)])

for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:  # 토마토가 익은 곳을 BFS 탐색 대상으로 추가
                queue.append((i,j,k))

print(BFS())