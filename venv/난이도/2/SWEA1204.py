a = int(input())
for test_case in range(1, a + 1):
    b = input()
    test = list(map(int, input().strip().split()))
    count = [0]*101
    for i in test:
        count[i]+=1
    c = max(count)
    for j in range(100,0,-1):
        if count[j] == c:
            print(f"#{test_case} {j}")
            break