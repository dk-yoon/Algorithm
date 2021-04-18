'''
BOJ1759 - 암호 만들기 (수학, 브루트포스 알고리즘, 조합론, 백트래킹)
'''

L, C = map(int, input().split())
arr = list(map(str, input().split()))
used = [False] * len(arr)
order = []
sorted_order = []
vowel = ['a', 'e', 'i', 'o', 'u']

def quick_sort(arr):    # 시간초과나서 내장 sort 대체하여 퀵정렬 사용
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

def comb(k, n): # 부분집합 조합
    if k == n:
        sorted_order.append(quick_sort(order))
        return

    for i in range(n):
        if used[i]:
            break
        used[i] = True
        order.append(arr[i])
        comb(k + 1, n)
        used[i] = False
        order.pop()

comb(C-L, C)
sorted_order = quick_sort(sorted_order)

for ans in sorted_order:
    count = 0
    for vow in vowel:
        if vow in ans:  # 암호당 모음의 갯수 카운트
            count += 1
    if 1 <= count <= L-2:   # 모음 카운트가 해당 범위 안이면 자음도 자동으로 요건 충족
        print(''.join(ans))