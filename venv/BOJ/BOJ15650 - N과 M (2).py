'''
BOJ15650 - N과 M (2) (백트래킹)
'''

arr = "12345678" # 1 <= M <= N <= 8
order = []                  # 순열 저장
used = [False] * len(arr)   # 사용 여부 기록
N, M = map(int, input().split()) # 문제에서 제시되는 조건 자연수
answer = []

def comb(k, n):
    if k == n:
        answer.append(sorted(order))
        return

    for i in range(n):
        if used[i]:
            break

        used[i] = True
        order.append(arr[i])

        comb(k + 1, n)

        used[i] = False
        order.pop()

comb(N-M, N)
answer.sort()
for ans in answer:
    print(' '.join(ans))