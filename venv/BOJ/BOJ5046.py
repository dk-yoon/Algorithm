'''
BOJ5046. 전국 대학생 프로그래밍 대회 동아리 연합
첫째 줄에 대회를 개최할 수 있으면 최소 비용을 출력하고, 없으면 "stay home"을 출력한다.
'''
N, B, H, W = map(int, input().split(' '))
charge = [0] * H
contain = [0] * H
minimum_charge = 500001

for h in range(H):
    charge[h] = int(input())
    contain[h] = list(map(int, input().split(' ')))

for i in range(len(charge)):
    if charge[i] * N <= B:
        for j in range(len(contain[i])):
            if int(contain[i][j]) >= N:
                if int(charge[i]) * N <= minimum_charge:
                    minimum_charge = charge[i] * N
if minimum_charge != 500001:
    print(minimum_charge)
else:
    print("stay home")