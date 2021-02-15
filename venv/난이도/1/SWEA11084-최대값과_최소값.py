'''
SWEA11084 - 최대값과 최소값
'''

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    num_list = list(map(int, input().split()))
    max_index = 0
    min_index = 0
    for i in range(N):
        if num_list[i] >= num_list[max_index]:
            max_index = i
    for j in range(N-1, -1, -1):
        if num_list[j] <= num_list[min_index]:
            min_index = j
    print(f'#{t} {abs(max_index-min_index)}')