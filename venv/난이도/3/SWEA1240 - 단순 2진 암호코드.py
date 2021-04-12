'''
SWEA1240 - 단순 2진 암호코드
'''

# 문제 지문 속 이미지 참조 (각 숫자별 코드)
code_dic = {'0001101': 0,
             '0011001': 1,
             '0010011': 2,
             '0111101': 3,
             '0100011': 4,
             '0110001': 5,
             '0101111': 6,
             '0111011': 7,
             '0110111': 8,
             '0001011': 9}

def find_code(data):
    global N,M,code
    for r in range(N):
        for c in range(M-1,-1,-1):
            # 코드 뒤부터 탐색하여 마지막 1인 부분을 기준으로 코드에 해당하는 부분을 추려냄
            if data[r][c] == '1':
                code = data[r][c-55:c+1]   # 암호문의 가로길이는 56
                return code
            
for tc in range(1, int(input()) + 1):
    N, M = map(int,input().split()) # 배열의 세로길이, 가로길이
    data = [input() for _ in range(N)]  # 0을 포함한 전체 코드
    code = ''
    find_code(data)
    answer = []

    start = 0
    end = 7

    for _ in range(8):  # 코드 딕셔너리에 맞는 코드를 찾아 배열에 저장, 7글자씩 8번 반복 = 길이 56
        answer.append(code_dic[code[start:end]])
        start += 7
        end += 7

    #  “(홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수
    ans = (answer[0] + answer[2] + answer[4] + answer[6]) * 3 +(answer[1] + answer[3] + answer[5]) + answer[7]

    # 10의 배수가 맞을 때 : 정상코드
    if not ans % 10:
        print("#{} {}".format(tc, sum(answer)))

    # 10의 배수가 아닐 때 : 비정상코드
    else:
        print("#{} {}".format(tc, 0))