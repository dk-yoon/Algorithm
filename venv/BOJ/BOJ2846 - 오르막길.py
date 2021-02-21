'''
BOJ2846 - 오르막길 (구현)
'''

N = int(input())
max_sum = -1
height_sum = 0
height_list = list(map(int, input().split()))

for i in range(1, N):
    gap = height_list[i] - height_list[i-1] # 해당 높이와 이전 높이의 차를 gap으로 지정

    if gap > 0:
        height_sum += gap
        if height_sum > max_sum: # 차이가 양수일경우 오르막길이므로 합을 더해감
            max_sum = height_sum # 합이 최대보다 커질 경우 최대합 갱신
    else:
        height_sum = 0  # 오르막길이 끝날 때 합을 다시 초기화

if max_sum == -1:   # 최대 합이 초기화 된 -1 그대로라면 0 출력
    print(0)
else:
    print(max_sum)