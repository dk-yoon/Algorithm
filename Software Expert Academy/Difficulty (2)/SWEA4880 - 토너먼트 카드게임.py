'''
SWEA4880 - 토너먼트 카드게임 (D2)
'''
def win(i, j):
    if (arr[i] == 1 and arr[j] == 3) or (arr[i] == 1 and arr[j] == 1):  # 가위 - 보 / 가위 - 가위
        return i
    elif (arr[i] == 2 and arr[j] == 1) or (arr[i] == 2 and arr[j] == 2): # 바위 - 가위 / 바위- 바위
        return i
    elif (arr[i] == 3 and arr[j] == 2) or (arr[i] == 3 and arr[j] == 3): # 보 - 바위 / 보 - 보
        return i
    else:   # j가 이긴 경우
        return j

def match(start, end):
    if start == end: # 최종 하나만 남았을 때
        return start

    first = match(start, (start+end)//2) # 처음 / 중간
    second = match((start+end)//2+1, end) # 중간 다음 / 끝
    return win(first, second)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0)    # 계산 용이를 위해 0번 인덱스에 값을 하나 추가
    print('#{} {}'.format(t, match(1, N)))