'''
종민이의 집에서 한 달간 사용하는 수도의 양이 W리터라고 할 때, 요금이 더 저렴한 회사를 골라 그 요금을 출력하는 프로그램을 작성하라.
'''
t = int(input())
charge = 0
for t in range (1,t+1):
    P, Q, R, S, W = map(int, input().split(' '))
    A = W * P
    if W > R :
        B = Q + (W - R) * S
    else:
        B = Q
    if A > B:
        charge = B
        print(f'#{t} {charge}')
    else:
        charge = A
        print(f'#{t} {charge}')
