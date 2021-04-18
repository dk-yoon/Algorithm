'''
총 데이터의 개수는 항상 a의 b제곱의 형태로 주어진다. 재용이는 문득 마지막 데이터가 처리될 컴퓨터의 번호가 궁금해졌다. 이를 수행해주는 프로그램을 작성하라
'''
T = int(input())

for t in range(T):
    a, b = map(int, input().split())
    a = a % 10

    if a == 0:
        print(10)
    elif a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 4 or a == 9:
        b = b % 2
        if b == 1:
            print(a)
        else:
            print((a * a) % 10)
    else:
        b = b % 4
        if b == 0:
            print((a ** 4) % 10 % 10 % 10)
        else:
            print((a ** b) % 10 % 10 % 10)