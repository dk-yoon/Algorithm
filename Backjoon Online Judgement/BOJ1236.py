'''
BOJ1236. 성지키기
성의 크기와 경비원이 어디있는지 주어졌을 때, 몇 명의 경비원을 최소로 추가해야 영식이를 만족시키는지 구하는 프로그램을 작성하시오.
'''
n, m = map(int, input().split())
castle = []
hor_count = m
ver_count = 0
for ver in range (n):
    castle.append(input())
for ver in range (n):
    if 'X' not in castle[ver]:
        ver_count += 1
for hor in range (m):
    for ver in range (n):
        if castle[ver][hor] ==  'X':
            hor_count -= 1
            break
print (max(hor_count, ver_count))
