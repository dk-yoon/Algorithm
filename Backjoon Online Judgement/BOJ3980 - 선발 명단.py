'''
BOJ3980 - 선발명단 (브루트포스 알고리즘, 백트래킹)
'''

def dfs(idx, arr_total):
    global max_total
    if idx == 11:
        if arr_total > max_total:
            max_total = arr_total   # 최대 능력치 갱신
        return

    for i in range(11):
        if arr[idx][i] == 0 or visit[i]:    # 능력치가 0이거나 이미 배치한 경우
            continue
        visit[i] = 1
        dfs(idx + 1, arr_total + arr[idx][i])   # row를 바꿔가면서 옆으로 탐색해감, 이미 탐색한 인덱스였으면 더이상 진행 X
        visit[i] = 0

C = int(input())
for c in range(C):
    arr = []
    for _ in range(11):
        arr.append(list(map(int, input().split())))
    visit = [0] * 11
    max_total = -1
    dfs(0, 0)   # 탐색 시행 (인덱스 0, 합계 0부터 시작)
    print(max_total)
