'''
BOJ1063. 킹 (구현, 시뮬레이션)
킹과 돌의 마지막 위치를 구하는 프로그램을 작성하시오.
'''
'''
A1 A2 5
B
L
LB
RB
LT
'''
input_King, input_Stone, N = map(str, input().split())
move_list = [] * int(N)
king_location = list(input_King)
king_location[0] = ord(king_location[0]) - 65
king_location[1] = int(king_location[1])-1
stone_location = list(input_Stone)
stone_location[0] = ord(stone_location[0]) - 65
stone_location[1] = int(stone_location[1])-1
# print(king_location)
# print(stone_location)

for n in range(int(N)):
    move_list.append(input())

# print(move_list)
for move in move_list:
    if move == 'R':
        king_location[0] += 1
        if king_location[0] == 8:
            king_location[0] -= 1
        if king_location == stone_location:
            stone_location[0] += 1
        if stone_location[0] == 8:
            stone_location[0] -= 1
            king_location[0] -= 1

    elif move == 'L':
        king_location[0] -= 1
        if king_location[0] == -1:
            king_location[0] += 1
        if king_location == stone_location:
            stone_location[0] -= 1
        if stone_location[0] == -1:
            stone_location[0] += 1
            king_location[0] += 1

    elif move == 'B':
        king_location[1] -= 1
        if king_location[1] == -1:
            king_location[1] += 1
        if king_location == stone_location:
            stone_location[1] -= 1
        if stone_location[1] == -1:
            stone_location[1] += 1
            king_location[1] += 1

    elif move == 'T':
        king_location[1] += 1
        if king_location[1] == 8:
            king_location[1] -= 1
        if king_location == stone_location:
            stone_location[1] += 1
        if stone_location[1] == 8:
            stone_location[1] -= 1
            king_location[1] -= 1

    elif move == 'RT':
        king_location[0] += 1
        king_location[1] += 1
        if king_location[0] == 8 or king_location[1] == 8:
            king_location[0] -= 1
            king_location[1] -= 1
        if king_location == stone_location:
            stone_location[0] += 1
            stone_location[1] += 1
        if stone_location[0] == 8 or stone_location[1] == 8:
            stone_location[0] -= 1
            stone_location[1] -= 1
            king_location[0] -= 1
            king_location[1] -= 1

    elif move == 'LT':
        king_location[0] -= 1
        king_location[1] += 1
        if king_location[0] == -1 or king_location[1] == 8:
            king_location[0] += 1
            king_location[1] -= 1
        if king_location == stone_location:
            stone_location[0] -= 1
            stone_location[1] += 1
        if stone_location[0] == -1 or stone_location[1] == 8:
            stone_location[0] += 1
            stone_location[1] -= 1
            king_location[0] += 1
            king_location[1] -= 1

    elif move == 'RB':
        king_location[0] += 1
        king_location[1] -= 1
        if king_location[0] == 8 or king_location[1] == -1:
            king_location[0] -= 1
            king_location[1] += 1
        if king_location == stone_location:
            stone_location[0] += 1
            stone_location[1] -= 1
        if stone_location[0] == 8 or stone_location[1] == -1:
            stone_location[0] -= 1
            stone_location[1] += 1
            king_location[0] -= 1
            king_location[1] += 1

    elif move == 'LB':
        king_location[0] -= 1
        king_location[1] -= 1
        if king_location[0] == -1 or king_location[1] == -1:
            king_location[0] += 1
            king_location[1] += 1
        if king_location == stone_location:
            stone_location[0] -= 1
            stone_location[1] -= 1
        if stone_location[0] == -1 or stone_location[1] == -1:
            stone_location[0] += 1
            stone_location[1] += 1
            king_location[0] += 1
            king_location[1] += 1

king_location[0] = chr((king_location[0]) + 65)
king_location[1] = str(king_location[1]+1)
stone_location[0] = chr((stone_location[0]) + 65)
stone_location[1] = str(stone_location[1]+1)
print(''.join(king_location))
print(''.join(stone_location))