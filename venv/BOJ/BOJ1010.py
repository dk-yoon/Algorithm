'''
BOJ1010. 다리 놓기 (수학, 다이나믹 프로그래밍, 조합론)
다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
'''
T = int(input())
N, M = map(int,input().split(' '))
bridges = [0] * N

for t in range(T):
    for m in range(0,M):
        for n in range(0, N):
            bridges[n] = m
    print(bridges)