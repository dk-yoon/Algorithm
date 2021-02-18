T = int(input())
for t in range(1, T + 1):
    str1 = sorted(set(input()))
    str2 = list(map(str, input()))
    max_count = 0
    for alphabet in str1:
        if str2.count(alphabet) >= max_count:
            max_count = str2.count(alphabet)
    print('#{} {}'.format(t, max_count))