n = 0
while n < 3:
    print(n)
    n = n+1
    print('반복중..')
print('반복문 탈출!')

dusts = [39, 42, 10]
for dust in dusts:
    print(dust)


numbers = [1,2,3,4,5,6,7]
number = 0
# 홀수만 찾아서 그 값을 출력하세요
for number in numbers:
    if (number % 2) == 1:
        print((f'{number}는 홀수입니다.'))