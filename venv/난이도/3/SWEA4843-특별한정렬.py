'''
SWEA4843 - 특별한 정렬 (D3)
'''
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    large_arr = []
    arr.sort()
    for n in range(N-1,N-6,-1):
        large_arr.append(arr[n])
    print(f'#{t} {arr[N-1]} {arr[0]} {arr[N-2]} {arr[1]} {arr[N-3]} {arr[2]} {arr[N-4]} {arr[3]} {arr[N-5]} {arr[4]}')
