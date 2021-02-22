'''
SWEA - 파스칼의 삼각형
'''
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    pascal = [[] for _ in range(10)]
    for n in range(N):
        if n == 0 :
            pascal[n].append(1)
        if n == 1 :
            pascal[n].append(1)
            pascal[n].append(1)
        if n > 1:
            pascal[n].append(1)
            for i in range(len(pascal[n-1])-1):
                pascal[n].append(pascal[n-1][i] + pascal[n-1][i+1])
            pascal[n].append(1)

    print('#{}'.format(t))
    for psc in pascal:
        if len(psc) > 0:
            for ps in psc:
                print(ps, end=" ")
            print()