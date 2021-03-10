'''
SWEA5099 - 피자굽기 (D3)
'''
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    lst_pizza= list(map(int, input().split()))  # 전체 피자 입력
    in_oven = []
    out_oven = []
    for i in range(N):
        in_oven.append((i+1, lst_pizza[i])) # 화덕에 들어간 피자 (순번, 남은 치즈양) 튜플로 구성

    for j in range(N, M):
        out_oven.append((j+1, lst_pizza[j])) # 화덕에 아직 못들어간 피자


    while len(in_oven) != 1:    # 화덕 내에 피자가 1개 남을 때까지 반복
        num, cheese = in_oven.pop(0)
        cheese //= 2 # 치즈양 절반으로 변경
        if cheese > 0: # 치즈가 남아 화덕에 머무르는 경우 큐 끝에 다시 추가
            in_oven.append((num, cheese))

        else:
            if len(out_oven) > 0: # 치즈가 0이 되었을때, pop한 상태로 넘어가며 남은 피자를 화덕에 투입
                in_oven.append(out_oven.pop(0))

    print('#{} {}'.format(t, in_oven.pop()[0])) # 마지막 남은 화덕 피자의 순번을 출력

