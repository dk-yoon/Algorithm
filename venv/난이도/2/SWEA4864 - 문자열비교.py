T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    flag = False

    # 두 문자열 길이의 차이만큼 반복
    for i in range(len(str2) - len(str1) + 1):
        # str2에서 str1 길이만큼 잘라낸 영역에서 str1과 같은게 있다면 True
        if str1 == str2[i:i+len(str1)]:
            flag = True
    if flag == True:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))