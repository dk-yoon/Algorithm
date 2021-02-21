'''
BOJ2846 - 오르막길 (구현)
'''

N = int(input())
max_sum = -1
height_sum = 0
height_list = list(map(int, input().split()))

for i in range(1, N):
    gap = height_list[i] - height_list[i-1]

    if gap > 0:
        height_sum += gap
        if height_sum > max_sum:
            max_sum = height_sum
    else:
        height_sum = 0

if max_sum == -1:
    print(0)
else:
    print(max_sum)