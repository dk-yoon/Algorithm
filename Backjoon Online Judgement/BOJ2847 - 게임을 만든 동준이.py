'''
BOJ2847 - 게임을 만든 동준이 (그리디 알고리즘)
'''
N = int(input())
score = []
count = 0

for n in range(N):
    score.append(int(input()))

# 3 8 5 5로 주어진 경우 answer : 3 4 5 error : 4 4 5
# for문으로 N번 더 돌려서 다시 오류를 가다듬음
for _ in range(N):
    for i in range(N-1):
        while True:
            if score[i] < score[i + 1]:
                break
            score[i] -= 1
            count += 1
print(count)
