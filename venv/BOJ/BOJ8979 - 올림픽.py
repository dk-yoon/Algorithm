'''
BOJ8979 - 올림픽 (정렬)
'''

N, K = map(int, input().split())
rank_table = []

for n in range(N):
    ranking = list(map(int, input().split()))
    if ranking[0] == K:
        standard = ranking  # 찾으려는 국가를 standard 변수로 지정
    else:
        rank_table.append(ranking)  # 그 외 국가들의 성적을 리스트에 추가

count = 1   # 기본값을 1등으로 보아서 1로 선언
for i in range(len(rank_table)):
    if rank_table[i][1] > standard[1]:  # 금메달 비교
        count += 1  # 비교 국가가 앞서는 국가이므로 순위를 한단계 뒤로

    elif rank_table[i][1] == standard[1]:
        if rank_table[i][2] > standard[2]:  # 은메달 비교
            count += 1

        elif rank_table[i][2] == standard[2]:
            if rank_table[i][3] > standard[3]:  # 동메달 비교
                count += 1

print(count)    # 찾으려는 국가보다 앞서는 국가 수만큼 count가 증가하였음