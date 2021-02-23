'''
SWEA4871 - 그래프 경로 (D2)
'''

# 재귀 사용
# def dfs(v):
#     visit[v] = 1
#     for w in G[v]:
#         if visit[w] == 0:
#             dfs(w)

def dfs(v):
    S = [v]
    visit[v] = 1
    while S:    # S 내에 데이터가 있는 동안
        for w in G[v]:  # 각 연결 탐색
            if visit[w] == 0:  # 연결되었지만 탐색을 안한 상태
                S.append(v)
                visit[w] = 1    # 탐색 완료 및 연결 상태 확인
                v = w   # 해당 노드를 시작점으로 계속 진행
                break

        else:
            v = S.pop() # 더 이상 탐색 할 노드가 존재하지 않음 빠져나와 재탐색

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split()) # V : 노드 갯수, E : 간선 갯수
    G = [[] for _ in range(V + 1)]  # 각 출발점이 연결된 도착점 리스트
    visit = [0] * (V + 1)  # 연결 여부 기록

    for _ in range(E):
        u, v = map(int, input().split()) # u와 v 사이 간선이 존재함 (단방향)
        G[u].append(v)  #  출발점이 연결된 도착점 리스트

    s, e = map(int, input().split())  # 확인할 시작 노드 s와 도착 노드 e
    dfs(s)  # 시작 노드를 기준으로 dfs
    print('#{} {}'.format(t, visit[e]))  # 도착 노드의 visit 여부를 확인