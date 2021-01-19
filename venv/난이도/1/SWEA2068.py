'''
10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
'''

t = int(input())
for t in range (1,t+1):
    numbers = [int(number) for number in input().split()]


    def MaxValue(A):
        Temp = 0
        for i in A:
            if Temp == 0 or i > Temp:
                Temp = i
        print(f'#{t} {Temp}')


    MaxValue(numbers)
