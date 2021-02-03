'''
BOJ1259. 팰린드롬수
각 줄마다 주어진 수가 팰린드롬수면 'yes', 아니면 'no'를 출력한다.
'''
while True:
    word = list((input()))
    reversed_word = []
    for alphabet in word[::-1]:
        reversed_word.append(alphabet)

    if word == ['0']:
        break
    elif word == reversed_word:
        print('yes')
    else:
        print('no')
