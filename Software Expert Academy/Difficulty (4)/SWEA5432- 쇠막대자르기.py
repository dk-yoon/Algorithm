'''
SWEA5432 - 쇠막대 자르기 (D4)
'''
T = int(input())
for t in range(1, T + 1):
    iron_bar = input()
    count = 0
    ans = 0

    for i in range(len(iron_bar)):
        if iron_bar[i] == '(':
            count += 1
        else:
            count -= 1
            if iron_bar[i-1] == '(':
                ans += count
            else:
                ans += 1
    print('#{} {}'.format(t, ans))
