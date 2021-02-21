'''
BOJ2804 - 크로스워드 만들기 (구현)
'''

A, B = map(str, input().split())
N = len(A)
M = len(B)
cross_list = [['.'] * N for _ in range(M)] # 가로 N 세로 M 만큼 '.'이 들어간 크로스 리스트 생성

for i in range(N):
    if (A[i]) in B:
        same_word = (A[i])  # A를 기준으로 공통 철자를 찾아서 same_word 선언
        break

A_idx = A.find(same_word)   # find 함수를 통해 가장 먼저 등장하는 인덱스를 idx로 선언
B_idx = B.find(same_word)
cross_list[B_idx] = list(A) # 세로 열 인덱스 부분에 A 문장 가로로 등록

for j in range(M):
    cross_list[j][A_idx] = B[j] # 가로 열 인덱스 부분마다 B 문장 세로로 등록

for answer in cross_list:
    print(''.join(answer))  # 최종 결과 리스트를 조인하여 출력