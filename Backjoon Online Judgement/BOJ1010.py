'''
BOJ1010. 다리 놓기 (수학, 다이나믹 프로그래밍, 조합론)
다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
'''

# 처음에 시도하려 했던 것 = 전체 다리설치 가능 개수 - 조건을 불만족하는 다리 수 (교차되서 설치됐을 때)

T = int(input())

def factorial(a):
    if a == 1 or a == 0:
        return 1
    return a * factorial(a - 1)

for t in range (T):
    N, M = map(int, input().split(' '))
    print(int(factorial(M)/((factorial(M-N))*(factorial(N)))))  # nCr
                                                                # nPr / r!
                                                        # n! / ((n-r)! * (r!))