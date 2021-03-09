'''
BOJ2309 - 일곱 난쟁이 (브루트포스 알고리즘)
'''
height_list = []
for _ in range(9):
    height_list.append(int(input()))

choice = [0] * 7 # 일곱명이 담길 리스트

def comb(idx, start):
    if idx == 7:
        if sum(choice) == 100:  # 일곱명의 합이 100이 될 때, 정렬 후 출력
            choice.sort()
            for ans in choice:
                print(ans)
            return
    else:
        for i in range(start, 9):
            choice[idx] = height_list[i]
            comb(idx + 1, i + 1) # 9명 중 7명으로 구성되는 모든 조합 생성
comb(0, 0)
