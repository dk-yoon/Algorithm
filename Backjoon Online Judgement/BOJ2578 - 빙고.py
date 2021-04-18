'''
BOJ2578 - 빙고 (구현)
'''
def check_bingo(lst):
    bingos = 0  # 전체 빙고 발생 수
    # 행
    bingos += lst.count([1, 1, 1, 1, 1])  # 단순히 모두 1로 칠해진 행의 갯수 카운트

    # 열
    for j in range(5):      # 세로열 탐색을 진행하며 0이 발생하지 않는 경우 (전체가 1) 빙고로 카운트
        for i in range(5):
            if lst[i][j] == 0:
                break
        else:
            bingos += 1

    # 대각
    bingo_count2 = 0    # 우하향 대각선 탐색을 진행하며 연속으로 1이 5번 등장할 경우 빙고로 카운트
    for i in range(5):
        if lst[i][i] == 1:
            bingo_count2 += 1
            if bingo_count2 == 5:
                bingos += 1
        else:
            bingo_count2 = 0

    # 대각2
    bingo_count3 = 0    # 우상향 대각선 탐색을 진행하며 연속으로 1이 5번 등장할 경우 빙고로 카운트
    for i in range(4,-1,-1):
        if lst[i][4-i] == 1:
            bingo_count3 += 1
            if bingo_count3 == 5:
                bingos += 1
        else:
            bingo_count3 = 0
    return bingos

bingo = []
announce = []
check = [[0] * 5 for _ in range(5)]
announce_count = 0
flag = False

for _ in range(5):
    bingo.append(list(map(int, input().split())))

for _ in range(5):
    a, b, c, d, e = map(int, input().split())
    announce.append(a)
    announce.append(b)
    announce.append(c)
    announce.append(d)
    announce.append(e)

for anc in announce:    # 사회자 번호를 하나씩 탐색
    for col in range(5):
        for row in range(5):
            if anc == bingo[col][row] and flag == False:    # 사회자 번호와 일치하는 열 과 행 인덱스에 대해 체크
                check[col][row] = 1
                announce_count += 1
                if check_bingo(check) >= 3: # 함수를 통해 계산한 빙고의 수가 3개 이상일 때 답 출력
                    print(announce_count)
                    flag = True  # 빙고조건 만족 이후 추가적인 출력을 막기위해 flag 변환