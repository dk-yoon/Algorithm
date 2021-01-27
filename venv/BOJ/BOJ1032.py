N = int(input())            # 테스트할 문장 갯수
main_txt = list(input())    # 처음 등록되어 다른 문장과 비교 될 main 문장
answer = []                 # ?가 반영된 변형 문장이 저장될 answer 리스트

for n in range (1, N):      # 총 문장 수 -1 만큼 반복
    sub_txt = list(input()) # 비교할 문장 입력
    length_s = len(sub_txt)
    # length_m = len(main_txt)

    for i in range (length_s):
        if main_txt[i] != sub_txt[i]:
            answer.append('?')
        else:
            answer.append(sub_txt[i])
    main_txt = answer       # 비교대상 문장을 변형 문장으로 교체하여 다음 반복 진행
    answer = []

print (''.join(main_txt))