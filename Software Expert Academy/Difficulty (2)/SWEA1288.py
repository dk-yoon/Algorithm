'''
SWEA1288. 새로운 불면증 치료법 (D2)
'''
t = int(input())
every = [0,1,2,3,4,5,6,7,8,9]   # 모든 자연수가 들어간 비교용 리스트
check = []  # 자연수가 추가될 빈 리스트 생성
for t in range (1,t+1):
    n = int(input())
    count = 0
    while every != sorted(set(check)):  # 중복을 제거하고 차례대로 나열한 리스트가 같을 때까지 반복
            count += 1
            for number in str(n * count):   # *2로 하려다가 꼬였었는데 반복문 안에 count를 활용
                check.append(int(number))   # 빈 리스트 내에 숫자를 정수형으로 추가
                # print(f'{count} {sorted(set(check))}')
    else:
        print(f'#{t} {count * n}')  # 조건 만족 후 결과 출력
        check = []

