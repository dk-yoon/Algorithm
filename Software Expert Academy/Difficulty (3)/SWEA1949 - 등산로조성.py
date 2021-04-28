'''
SWEA1949 - 등산로 조성
'''

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def dfs(y, x, height, K_used, length):
    global longest

    if length > longest:    # 최장 등산로 갱신
        longest = length

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < N and 0 <= nx < N and visit[ny][nx] == 0:

            if arr[ny][nx] < height:    # 주변 높이가 현재 높이보다 낮을때 추가 탐색
                visit[y][x] = 1
                dfs(ny, nx, arr[ny][nx], K_used, length + 1)
                visit[y][x] = 0

            elif K_used == False and arr[ny][nx] - K < height:  #  공사가능하며 공사가능 높이인 K만큼 범위 내에 있을 때
                new_height = height - 1 # 현재 높이보다 1만큼만 작게 공사 (더 줄이면 이후 탐색에 영향)
                visit[y][x] = 1
                dfs(ny, nx, new_height, True, length + 1)
                visit[y][x] = 0

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    highest = -987654321
    longest = -987654321
    arr = []

    for y in range(N):
        arr.append(list(map(int, input().split())))

    for y in range(N):
        for x in range(N):
            if arr[y][x] > highest:  # 제일 높은 구간이 갱신되면 시작지점 초기화
                highest = arr[y][x]
                start_point = []

            if arr[y][x] >= highest: # 제일 높은 구간은 시작지점으로 추가
                start_point.append((y, x))

            else:   # 나머지 경우 패스
                continue


    for y, x in start_point:
        visit = [[0] * N for _ in range(N)] # 한번 시행마다 방문 초기화
        dfs(y, x, highest, False, 1)    # (y, x, 높이값, 공사가능여부, 등산로 길이)

    print(f"#{t} {longest}")