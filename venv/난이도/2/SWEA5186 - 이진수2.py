'''
SWEA5186 - 이진수2 (D2)
'''
T = int(input())
for t in range(1, T + 1):
    answer = ''
    N = float(input())  # 십진수 N
    div = 1
    for _ in range(12): #최대 12자리까지 진행

        div /= 2    # 매회 나누기 2

        if N // div == 1:   # 나누어지는지 확인
            answer += '1'   # 나누어지면 문자열 1 추가
            N %= div     # N은 나눈 이후의 나머지

            if N == 0:  # 나누기를 거듭하다가 N이 0이 되면 종료
                break
        else:
            answer += '0'   # 안 나누어지는 경우 0 추가

    # 반복문 이후 N이 0이 아니면 13자리 초과
    if N > 0:
        answer = 'overflow'

    print('#{} {}'.format(t, answer))