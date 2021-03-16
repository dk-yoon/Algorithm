'''
BOJ17471 - 게리맨더링 (그래프 이론, 그래프 탐색, 브루트포스 알고리즘)
'''

def check_conn(lst):
    que = []
    visited = [0] * (N+1)
    que.append(lst[0])
    visited[lst[0]] = 1 # 시작점 방문 표시
    cnt = 0
    flag = False  # 서로 연결되었는지 여부
    while que:
        i = que.pop(0)
        cnt += 1
        for j in lst:
            if G[i][j] == 1 and visited[j] == 0:  # i와 j 도시가 연결되어있고 탐색이 안되었으면
                que.append(j)   # 큐에 추가
                visited[j] = 1  # i 출발 j 도착 방문기록
    if cnt == len(lst):
        flag = True    # 연결된 모든 도시를 방문할 수 있었을 때 true
    return flag

def sum_pop(lst):
    sum = 0
    for i in lst:
        sum += pop[i]
    return sum  # 연결 도시들의 인구합 반환

def powerset(k):
    global ans
    if k == N+1:
        A = []
        B = []
        for i in range(1, N+1):
            if include[i]:  # A 포함 지역
                A.append(i)
            else:
                B.append(i) # B 포함 지역
        if len(A) != N and len(A) != 0 and len(B) != N and len(B) != 0: # 두 선거구가 적어도 하나 포함
            if check_conn(A) and check_conn(B): # 각 선거구 내 구역이 모두 연결되어 있는지 체크
                gap = abs(sum_pop(A) - sum_pop(B))  # 인구차이 계산
                if ans > gap:
                    ans = gap   # 최저 인구차이 갱신
        return
    include[k] = 1
    powerset(k+1)
    include[k] = 0
    powerset(k+1)   # 부분집합 재귀 공식


N = int(input())
pop = list(map(int, input().split()))
pop.insert(0,0)
G = [[0 for _ in range(N+1)] for _ in range(N+1)]   # 인접행렬
include = [0] * (N+1)   # 선거구 포함여부
ans = 987654321

for u in range(1, N+1):
    temp = list(map(int, input().split()))
    for j in range(1, temp[0]+1):
        v = temp[j] # 도시간 서로 연결 1: A 0: B
        G[u][v] = 1
        G[v][u] = 1

powerset(1)
print(-1 if ans == 987654321 else ans)