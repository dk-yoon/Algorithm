'''
BOJ2804 - 크로스워드 만들기 (구현)
'''

A, B =map(str, input().split())
N = len(A)
M = len(B)
cross_list = [['.'] * N for _ in range(M)]

for i in range(N):
    if (A[i]) in B:
        same_word = (A[i])
        break

A_idx = A.find(same_word)
B_idx = B.find(same_word)
cross_list[B_idx] = list(A)

for j in range(M):
    cross_list[j][A_idx] = B[j]

for answer in cross_list:
    print(''.join(answer))