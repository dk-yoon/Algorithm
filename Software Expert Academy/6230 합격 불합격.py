score = [88,30,61,55,95]
for i in range(0,5):
    if score[i] >= 60:
        print(str(i+1)+"번 학생은 "+str(score[i])+"점으로 합격입니다.")
    else:
        print(str(i + 1) + "번 학생은 " + str(score[i]) + "점으로 불합격입니다.")