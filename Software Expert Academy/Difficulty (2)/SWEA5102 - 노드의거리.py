'''
SWEA5102 - 노드의 거리 (D2)
'''
def BFS(Q):
    count = 1
    while Q:
        next_Q = []
        while Q:
            index = Q.pop()
            for i in Relation[index]:
                if visit[i]:
                    continue
                if i == G:
                    return count
                next_Q.append(i)
                visit[i] = 1
        count += 1
        Q = next_Q
    return 0


for t in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    Relation = [[] for _ in range(V + 1)]
    visit = [0 for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        Relation[u].append(v)
        Relation[v].append(u)

    S, G = map(int, input().split())
    visit[S] = 1

    print('#{} {}'.format(t, BFS([S])))