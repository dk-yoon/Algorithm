# SWEA6485. 삼성시의 버스노선 (Difficulty : 3)
# P개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램을 작성하라.

# 테스트 케이스 수
T = int(input())

for t in range(1, T + 1):
    # N : 버스 노선의 수
    N = int(input())
    A = [0] * N
    B = [0] * N
    # 각 노선별 A와 B를 입력받음 (출발점과 도착점)
    for n in range(N):
        A[n], B[n] = map(int, input().split())
        # print(A, B)
    # P = 물어볼 정류장의 수
    P = int(input())

    count = [0] * 5000  # 최대 5000개의 정류장 존재
    index = [0] * P     # 물어볼 P 갯수만큼의 인덱스 리스트
    answer = []         # 최종 각 p에 해당하는 방문 버스 수 저장

    # 각 버스 노선마다 출발점과 끝점동안의 카운트를 1씩 증가시킨다
    for n in range(N):
        for i in range(A[n]-1, B[n]):
            count[i] += 1

    # 전체 P번동안 물어보는 p번 정류장의 순서를 기억한다
    for p in range(P):
        index[p] = int(input())

    # p번 정류장의 순서대로 (물어본 순서대로), 방문 버스 수를 추가한다.
    for j in index:
        answer.append(str(count[j-1]))

    # 최종 출력 진행
    answer = ' '.join(answer)
    print(f'#{t} {answer}')