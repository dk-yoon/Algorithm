'''
10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력하는 프로그램을 작성하라.
'''
t = int(input())
sum = 0
for t in range (1,t+1):
    numbers = [int(number) for number in input().split()]
    for i in range (0, 10):
        if numbers[i] % 2 == 1:
            sum += (numbers[i])
    answer = (sum)
    print(f'#{t} {answer}')
    sum = 0