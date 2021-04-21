'''
SWEA5208 - 전기버스2 (D3)
'''
from collections import deque

def dfs(i, total):
    global answer
    if answer < total:  # 이동횟수가 최소보다 커지면 중단
        return
    if i >= N:  # 최종 도착지와 같거나 넘어섰을 때, 이동횟수 기록 후 중단
        answer = total
        return
    count = station[i]
    for j in range(count, 0, -1):   # 최고 이동거리부터 탐색 진행
        dfs(i + j, total + 1)

T = int(input())
for t in range(1, T + 1):
    answer = 987654321  # 최소 이동횟수
    station = deque(map(int, input().split()))
    N = station.popleft() - 1   # 초기 스타트를 제외하기 위해 -1
    dfs(0, -1)  # 가장 처음 추가되는 total 값을 고려하여 -1
    print(f'#{t} {answer}')