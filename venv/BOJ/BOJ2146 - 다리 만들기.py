'''
BOJ2146 - 다리 만들기 (그래프 이론, 그래프 탐색, BFS)
'''

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

N = int(input())
arr = []
for n in range(N):
    arr.append(list(map(int, input().split())))

coast = [[0] * N for _ in range(N)]
visit = [[0] * N for _ in range(N)]
zone = 1

# 섬마다 다른 숫자값 설정
for y in range(N):
    for x in range(N):
        if arr[y][x] == 1 and visit[y][x] == 0: # 아직 방문하지 않은 섬 큐에 추가
            visit[y][x] = 1
            arr[y][x] = zone  # 탐색완료 시 zone을 증가시켜 각 섬 구별
            q = deque()
            q.append((y, x))

            while q:
                y, x = q.pop()
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0:
                        if arr[ny][nx] == 1:
                            visit[ny][nx] = 1
                            arr[ny][nx] = zone  # 각 섬마다 zone 넘버 체킹
                            q.append((ny, nx))  # 탐색
                        else:   # 탐색 위치에 바다가 있을 때
                            coast[y][x] = True  # 상하좌우에 바다가 있는 칸 기록
            zone += 1   # 다음번 탐색 때는 증가된 zone값 적용

# 최단거리 탐색
ans = 987654321

for y in range(N):
    for x in range(N):
        if coast[y][x] == 1: # 바다 인근인 부분
            visit = [[0] * N for n in range(N)]
            visit[y][x] = 1
            
            zone = arr[y][x]  # 현재 탐색하는 곳의 zone을 읽어옴
            q = deque()
            q.append((y,x,0))
            distance = 987654321
            while q:
                y, x, cnt = q.popleft()

                if arr[y][x] and arr[y][x] != zone: # 바다가 아니며 현재 설정된 섬과 다른 곳에 도착했다면
                    distance = cnt - 1 # 추가탐색한 1만큼을 빼주고 탐색을 중지
                    break

                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    
                    if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0 and arr[ny][nx] != zone: # 방문 안한 상태이며 현재 섬과 다를 때 (바다 또는 다른 섬)
                        visit[ny][nx] = 1
                        q.append((ny, nx, cnt + 1)) # 누적 거리를 기록하며 탐색

            if distance < ans:  # 최저 거리 갱신
                ans = distance
print(ans)