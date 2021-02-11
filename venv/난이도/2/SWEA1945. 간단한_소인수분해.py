T = int(input())
for t in range(1, T + 1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0

    while True:
        if N % 2 != 0:
            break
        else:
            N = N / 2
            a += 1

    while True:
        if N % 3 != 0:
            break
        else:
            N = N / 3
            b += 1

    while True:
        if N % 5 != 0:
            break
        else:
            N = N / 5
            c += 1

    while True:
        if N % 7 != 0:
            break
        else:
            N = N / 7
            d += 1

    while True:
        if N % 11 != 0:
            break
        else:
            N = N / 11
            e += 1

    print(f'#{t} {a} {b} {c} {d} {e}')