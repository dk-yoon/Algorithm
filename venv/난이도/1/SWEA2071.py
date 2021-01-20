'''
10개의 수를 입력 받아, 평균값을 출력하는 프로그램을 작성하라.

(소수점 첫째 자리에서 반올림한 정수를 출력한다.)
'''
t = int(input())
sum = 0
for t in range (1,t+1):
    numbers = [int(number) for number in input().split()]
    for i in range (0, 10):
        sum += numbers[i]
    answer = round(sum/10)
    print(f'#{t} {answer}')
    sum = 0