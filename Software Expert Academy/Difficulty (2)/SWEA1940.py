t = int(input())
total = 0
for t in range (1,tc+1):
    for t in range (1, T+1):
        a, b = map(int, input().split())
        if b == 1:
            total += 1
        elif b == 2:
            total += 2
        elif b == 0:
            total += 1
        print (total)
