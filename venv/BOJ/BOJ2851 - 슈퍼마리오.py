'''
BOJ2851 - 슈퍼마리오 (구현)
'''
score_list = []
total = 0
flag = True

for i in range(10):
    score_list.append(int(input()))

for score in score_list:
    # 절댓값을 통한 비교
    # flag를 통해 중간에 멈추었는지 확인
    if abs(total-100) >= abs(total + score) - 100 and flag == True:
        total += score
    # 중간에서 멈추는 경우 flag 신호를 False로 변경
    else:
        flag = False

print(total)