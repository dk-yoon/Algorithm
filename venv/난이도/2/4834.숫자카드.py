'''
0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오.
카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
'''

T = int(input())
for t in range(1,T+1):
    N = int(input())
    total_numbers = list(map(int,input()))

    max_num = 0
    max_count = 0
    for number in sorted(total_numbers):
        if total_numbers.count(number) >= max_count:
            max_count = total_numbers.count(number)
            max_num = number
    print(f'#{t} {max_num} {max_count}')