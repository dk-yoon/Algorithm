T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    multi_list = []
    max_list = -987654321

    if len(A) < len(B):
        while True:
            if len(A) == len(B)+1:
                break
            for i in range(len(A)):
                multi_list.append(A[i] * B[i])
            total = sum(multi_list)
            if total > max_list:
                max_list = total
            multi_list = []
            A.insert(0,0)
        print(f'#{t} {max_list}')

    elif len(A) > len(B):
        while True:
            if len(B) == len(A)+1:
                break
            for i in range(len(B)):
                multi_list.append(A[i] * B[i])
            total = sum(multi_list)
            if total > max_list:
                max_list = total
            multi_list = []
            B.insert(0,0)
        print(f'#{t} {max_list}')