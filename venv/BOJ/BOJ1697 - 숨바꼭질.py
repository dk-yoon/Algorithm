'''
BOJ1697 - 숨바꼭질 (그래프 이론, 그래프 탐색, BFS)
'''
from collections import deque

def bfs():
    q = deque()
    q.append(N)  # 시작 노드를 큐에 넣어줌
    while q:
        a = q.popleft()
        if a == K:
            print(cnt[a])
            break

        dx = [-1, 1, a]
        for i in range(3):
            na = a + dx[i]
            if 0 <= na <= 100000 and not cnt[na]:
                cnt[na] = cnt[a] + 1
                q.append(na)

cnt = [0] * 100001
N, K = map(int, input().split())

bfs()