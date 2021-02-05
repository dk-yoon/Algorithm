'''
BOJ1316. 그룹 단어 체커 (분류, 구현, 문자열)
단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
'''
T = int(input())
count = 0
words = []
flag = None

for t in range(T):
    words.append(input())

for word in words:
    for i in range(len(word)):
        if (word.find(word[i], i+1) - i) > 1:
            flag = False
            break
        else:
            flag = True
    if flag == True:
        count += 1

print(count)
