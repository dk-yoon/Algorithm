a = int(input())
for test_case in range(1, a + 1):
    b = input()
    tests = list(map(int, input().strip().split()))
    count = [0]*101
    c = max(count)
    for test in tests:
        count[test] += 1
    for j in range(100,0,-1):
        if count[j] == c:
            print(f"#{test_case} {j}")
            break