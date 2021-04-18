'''
N개의 양의 정수에서 가장 큰 수와 가장 작은 수의 차이를 출력하시오.
'''
T = int(input())
for t in range(1,T+1):
    _ = int(input())
    min_num = 1000000
    max_num = 1
    numbers = list(map(int,input().split()))

    for number in numbers:
        if number < min_num:
            min_num = number
        elif number > max_num:
            max_num = number

    print(f'#{t} {max_num-min_num}')