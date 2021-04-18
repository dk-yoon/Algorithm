'''
BOJ2798 - 블랙잭 (브루트포스 알고리즘)
'''
N, M = map(int, input().split())
nums = list(map(int, input().split()))
R = 3
min_gap = 987654321

choice = [0] * R
def comb(idx, start):
    global min_gap, ans
    if idx == R:
        if 0 <= M - sum(choice) <= min_gap:
            min_gap = M - sum(choice)
            ans = sum(choice)
        else:
            pass
    else:
        for i in range(start, N):
            choice[idx] = nums[i]
            comb(idx + 1, i + 1)
comb(0, 0)
print(ans)