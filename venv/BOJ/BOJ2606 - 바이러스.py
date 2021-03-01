'''
BOJ2606 - 바이러스 (그래프 이론, 그래프 탐색, BFS, DFS)
'''

# DFS 반복문 인접리스트 활용

def DFS(v):
    S = []  # 스택 생성
    S.append(v) # 기준 개체 추가
    visit[v] = True # 자기 자신에 대한 방문여부 기록
    answer.append(v) # 답안 계산을 위해 별도 리스트에 추가

    while len(S):
        for w in G[v]:
            if not visit[w]:    # 연결 리스트에는 있으나 아직 방문체크를 안한 경우
                S.append(v)     # 스택에 개체 추가
                v = w   # 차후 순회할 개체 변경
                visit[w] = True # 방문 여부 기록
                answer.append(v)    # 답안 계산을 위한 별도 리스트 추가
                break
        else:   # 연결 리스트에 있으나 이미 방문 확인을 마친 경우
            v = S.pop() # 스택 밖으로 나와 다른 대상 탐색

V = int(input())    # 전체 개체 수
E = int(input())    # 관계의 수
G = [[] for _ in range(V + 1)]  # 해당 개체에 연결된 개체들을 표현하는 리스트 (0은 고려안하므로 +1 하여 진행)
answer= []  # 문제의 답안 출력을 돕기위한 리스트
visit = [False for _ in range(V + 1)]   # 개체 방문 여부를 확인하기 위한 리스트

for i in range(E):  # 각 연결관계 대상
    u, v = map(int, input().split())
    G[u].append(v)  # 서로 연결된 각 개체에 대해 G 리스트 추가
    G[v].append(u)

DFS(1)  # 1번 컴퓨터와 연결된 개체를 계산하는 함수
print(len(answer)-1)    # 1번 본인을 제외한 연결 개체 수 출력
