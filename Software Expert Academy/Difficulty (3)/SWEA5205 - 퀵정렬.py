'''
SWEA5205 - 퀵 정렬 (D3)
'''
def quickSort(arr, lo, hi):
    if lo < hi:
        i, j = lo, hi

        while i < j:
            while i <= hi and arr[i] <= arr[lo]:
                i += 1

            while arr[j] > arr[lo]:
                j -= 1

            if i >= j: break

            arr[i], arr[j] = arr[j], arr[i]

        arr[lo], arr[j] = arr[j], arr[lo]

        quickSort(arr, lo, j - 1)
        quickSort(arr, j + 1, hi)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    quickSort(arr, 0, len(arr) - 1)

    print(f'#{t} {arr[N//2]}')
