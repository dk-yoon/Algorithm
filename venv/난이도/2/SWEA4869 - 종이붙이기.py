'''
SWEA4869 - 종이 붙이기 (D2)
'''
# 10 : 1, 20 : 3, 30 : 5, 40 : 11, 50: 21
def rectangle(N):
    if N == 10:
        return 1
    elif N == 20:
        return 3
    else:
        return (2 * rectangle(N - 20)) + (rectangle(N - 10))

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(t, rectangle(N)))