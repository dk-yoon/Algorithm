'''
충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
'''
T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int,input().split())
    station = [0] * N
    count = 0
    move = 0
    M = list(map(int, input().split()))
    for m in M:
        station[m] = 1

    while (move + K < N):
        for j in range(K, -1, -1):
            if j == 0:
                count = 0
                move += N
            elif station[move + j] == 1:
                move += j
                count += 1
                break
    print(f'#{t} {count}')
    
