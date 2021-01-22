'''
SWEA1285 (D2)
'''
t = int(input())
for t in range (1,t+1):
    min_p = 1000000
    count = 1
    n = int(input())
    throws = list(map(int, input().strip().split()))
    for throw in throws:
        p = abs(throw)
        if p < min_p:
            min_p = p
        elif p == min_p:
            count += 1
    print(f'#{t} {min_p} {count}')
