'''
BOJ1018. 체스판 다시 칠하기 (브루트포스 알고리즘)
지민이가 다시 칠해야 하는 정사각형의 최소 개수를 구하는 프로그램을 작성하시오.
'''
N, M = map(int, input().split(' '))
board = []
for n in range(N):
    board.append(list(map(str, input())))

w_board = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

b_board =[['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
 ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
 ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]



def compare(move_board):
    count_w = 0 # 화이트로 시작하는 보드와 비교했을 때
    count_b = 0 # 블랙으로 시작하는 보드와 비교했을 때
    for i in range(8):
        for j in range(8):
            if w_board[i][j] != move_board[i][j]:   # 기존 정석 보드와 비교했서 차이가 있을 경우 카운트 + 1
                count_w += 1
            if b_board[i][j] != move_board[i][j]:
                count_b += 1
    return min(count_w, count_b)

min_count = 64  # 모든 개체가 틀렸을 경우, 64개 (최대값으로 설정해놓음)

for x in range(0, N-7):
    for y in range(0, M-7):
        second_map = []
        second_map.append(board[x][y:y + 8])
        second_map.append(board[x + 1][y:y + 8])
        second_map.append(board[x + 2][y:y + 8])
        second_map.append(board[x + 3][y:y + 8])
        second_map.append(board[x + 4][y:y + 8])
        second_map.append(board[x + 5][y:y + 8])
        second_map.append(board[x + 6][y:y + 8])  
        second_map.append(board[x + 7][y:y + 8])    # 도움받음, 8*8 격자를 이동하는 부분
                                                    # y = M-7까지 반복문이므로 y를 기준으로 x 쫘르르
        answer = compare(second_map)
        if min_count > answer:
            min_count = answer
        second_map.clear()

print(min_count)