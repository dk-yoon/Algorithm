'''
SWEA5097 - 회전 (D2)
'''
from collections import deque

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))

    for m in range(M):
        left_num = Q.popleft()
        Q.append(left_num)

    print('#{} {}'.format(t, Q[0]))