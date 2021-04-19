'''
SWEA11891 -  분할정복 병합정렬 (D3)
'''

def sorting(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    group1 = sorting(lst[:mid])
    group2 = sorting(lst[mid:])
    return merge(group1, group2)

def merge(group1, group2):
    global cnt

    len_group1 = len(group1)
    len_group2 = len(group2)
    result = [0] * (len_group1 + len_group2)
    g1_i, g2_i = 0, 0
    i = 0

    if group1[-1] > group2[-1]:
        cnt += 1

    while g1_i != len_group1 and g2_i != len_group2:
        if group1[g1_i] <= group2[g2_i]:
            result[i] += group1[g1_i]
            i += 1
            g1_i += 1
        else:
            result[i] += group2[g2_i]
            i += 1
            g2_i += 1

    if g1_i != len_group1:
        while g1_i != len_group1:
            result[i] += group1[g1_i]
            i += 1
            g1_i += 1

    if g2_i != len_group2:
        while g2_i != len_group2:
            result[i] += group2[g2_i]
            i += 1
            g2_i += 1

    return result


T = int(input())
for t in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    arr = sorting(lst)

    print(f'#{t} {arr[N//2]} {cnt}')