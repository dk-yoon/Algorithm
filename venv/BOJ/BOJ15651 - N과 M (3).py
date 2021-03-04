'''
BOJ15651 - N과 M (3) (백트래킹)
'''

arr = "12345678" # 1 <= M <= N <= 8
order = []                  # 순열 저장
used = [False] * len(arr)   # 사용 여부 기록
N, M = map(int, input().split()) # 문제에서 제시되는 조건 자연수

def perm(k, n): # k = (n-r) 출력 순열 길이와 n과의 차이, n = 순열에 사용할 수가 어디까지인지
    if k == n:  # (n-r)과 n이 같아지는 시점
        print(" ".join(order))
        return

    for i in range(n):
        order.append(arr[i])
        perm(k + 1, n)
        order.pop()

perm(N-M, N)
