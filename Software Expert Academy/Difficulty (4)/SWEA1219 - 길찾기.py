'''
SWEA1219 - 길찾기 (D4)
'''
def dfs(v):
    visit[v] = 1
    for w in G[v]:
        if visit[w] == 0:
            dfs(w)

T = 10
for _ in range(T):
    t, link_num = map(int, input().split())
    nod_num = 100
    G = [[] for _ in range(nod_num + 1)]
    u = []  # 시작점 모은 리스트
    v = []  # 도착점 모은 리스트
    uv_total = list(map(int, input().split()))
    visit = [0] * (nod_num + 1)

    for i in range(link_num):
        for uv in range(len(uv_total)):
            if uv % 2:
                v.append(uv_total[uv])
            else:
                u.append(uv_total[uv])
        G[u[i]].append(v[i])

    s = 0  # 시작 노드와 도착 노드는 0과 99로 제시됨
    e = 99

    dfs(s)  # 시작 노드를 기준으로 dfs
    print('#{} {}'.format(t, visit[e]))  # 도착 노드의 visit 여부를 확인
