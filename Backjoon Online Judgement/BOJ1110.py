'''
N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.
'''

N = list(input())

if len(N) < 2:
    N.insert(0, '0')  # N이 한자리 수 일 때, 가장 맨 앞에 '0'을 추가
# origin_N = N  # 처음 숫자와 비교를 위해 원본 N 저장 - 참조가 되버림
origin_N = N.copy()
count = 0

while True:
    if N == origin_N and count > 0:
        break
    num_add = ((int(N[0]) + int(N[1])) % 10)
    N[0] = N[1]
    N[1] = str(num_add)
    count += 1
print (count)
