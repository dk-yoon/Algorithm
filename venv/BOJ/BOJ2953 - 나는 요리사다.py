'''
BOJ2953 - 나는 요리사다 (수학, 구현, 사칙연산)
'''
participant = [0] * 5

for i in range(5):
    participant[i] += sum(list(map(int, input().split())))

score = max(participant)
idx = participant.index(score) + 1
print('{0} {1}'.format(idx, score))
