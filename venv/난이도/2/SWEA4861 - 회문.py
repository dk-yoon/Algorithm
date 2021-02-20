T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [0 for _ in range(N)]
    for i in range(N):
        arr[i] = list(input())
    count = 0
    print("#{} ".format(t), end="")

    for row in range(N):
        for start_point in range(N - M + 1):
            end_point = start_point + M - 1
            for move in range(M // 2):
                if arr[row][start_point + move] == arr[row][end_point - move]:
                    count += 1
            if count == M//2:
                for col in range(start_point, start_point + M):
                    print(arr[row][col], end="")
            count = 0

    count = 0
    for col in range(N):
        for start_point in range(N - M + 1):
            end_point = start_point + M - 1
            for move in range(M // 2):
                if arr[start_point + move][col] == arr[end_point - move][col]:
                    count += 1
            if count == M//2:
                for row in range(start_point, start_point + M):
                    print(arr[row][col], end="")
            count = 0
    print()