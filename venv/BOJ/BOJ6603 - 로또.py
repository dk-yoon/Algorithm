'''
BOJ6603 - 로또 (수학, 조합론, 백트래킹, 재귀)
'''
def comb(k, n):
    if k == n:
        answer.append(sorted(arr))
        return

    for i in range(n):
        if used[i]:
            break

        used[i] = True
        arr.append(nums[i])

        comb(k + 1, n)

        used[i] = False
        arr.pop()

while True:
    nums = list(map(int, input().split()))
    N = nums.pop(0) # 받았던 수 중 맨 첫번째는 N에 해당

    if N == 0:  # N값이 0일 경우 반복문 중단
        break

    arr = []  # 조합 저장
    used = [False] * N   # 사용 여부 기록
    answer = []

    comb(N-6, N)
    answer.sort()

    for answ in answer:
        for ans in answ:
            print(ans, end=' ')
        print()
    print()