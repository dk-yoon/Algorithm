'''
BOJ8979 - 올림픽 (정렬)
'''

N, K = map(int, input().split())
rank_table = []

for n in range(N):
    ranking = list(map(int, input().split()))
    if ranking[0] == K:
        standard = ranking
    else:
        rank_table.append(ranking)

count = 1
for i in range(len(rank_table)):
    if rank_table[i][1] > standard[1]:
        count += 1

    elif rank_table[i][1] == standard[1]:
        if rank_table[i][2] > standard[2]:
            count += 1

        elif rank_table[i][2] == standard[2]:
            if rank_table[i][3] > standard[3]:
                count += 1

print(count)