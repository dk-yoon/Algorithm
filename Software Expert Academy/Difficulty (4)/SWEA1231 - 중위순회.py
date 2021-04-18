'''
SWEA1231 - 중위순회 (D4)
'''

def inorder(v):
    if v == 0: return

    inorder(L[v])
    num_list.append(v)
    inorder(R[v])

for t in range(1, 11):
    V = int(input())
    E = V - 1
    L = [0] * (V + 1) # 부모를 인덱스로 왼쪽 자식번호 저장
    R = [0] * (V + 1) # 부모를 인덱스로 오른쪽 자식번호 저장
    P = [0] * (V + 1) # 자식을 인덱스로 부모번호 저장

    arr = []
    for v in range(V):
        arr.append(list(input().split()))


    for i in range(E):
        if len(arr[i]) == 4:     # 양쪽 존재
            n1 = int(arr[i][0])  # 부모 숫자
            n2 = int(arr[i][2])  # 왼쪽 자식숫자
            n3 = int(arr[i][3])  # 오른쪽 자식숫자

            L[n1] = n2
            R[n1] = n3
            P[n2] = n1
            P[n3] = n1

        elif len(arr[i]) == 3:  # 한쪽만 존재
            n1 = int(arr[i][0]) # 부모 숫자
            n2 = int(arr[i][2]) # 자식숫자
            if L[n1] == 0:
                L[n1] = n2
            else:
                R[n1] = n2
            P[n2] = n1

    num_list = []
    inorder(1)

    print(f'#{t} ', end='')
    for num in num_list:
        for ar in arr:
            if num == int(ar[0]):
                print(ar[1], end='')
    print()