'''
SWEA2814 - 최장경로 (D3)
'''

def longest(v, dist):
    global ans

    if ans < dist:
        ans = dist
    visited[v] = 1

    for adj in graph[v]:
        if visited[adj]:
            continue
        longest(adj, dist + 1)
    visited[v] = 0
    return

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N + 1)]
    ans = 1

    for i in range(0, M):
        graph[arr[i][0]].append(arr[i][1])
        graph[arr[i][1]].append(arr[i][0])
    visited = [0] * (N + 1)
    for i in range(1, N + 1):
        longest(i, 1)

    print(f'#{t} {ans}')