def BubbleSort(a):
    for i in range(len(a) - 1, 0, -1):
        for j in range(0, i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

for t in range(1, 11):
    N = int(input())
    buildings = list(map(int,input().split()))
    count = 0
    for i in range(2, N-2):
        neighbor = []
        left_2 = buildings[i] - buildings[i-2]
        left_1 = buildings[i] - buildings[i-1]
        right_2 = buildings[i] - buildings[i+2]
        right_1 = buildings[i] - buildings[i+1]

        if left_1 > 0 and left_2 > 0 and right_1 > 0 and right_2 > 0:
            neighbor.append(left_1)
            neighbor.append(left_2)
            neighbor.append(right_1)
            neighbor.append(right_2)
            BubbleSort(neighbor)
            count += neighbor[0]

    print(f'#{t} {count}')
