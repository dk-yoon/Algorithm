'''
SWEA1974 - 스도쿠검증 (D2)
'''

T = int(input())
for t in range(1, T + 1):
    puzzle = []
    check = []
    ans = []
    for _ in range(9):
        puzzle.append(list(map(int, input().split())))

    # 가로
    flag = False
    for row in puzzle:
        if sorted(row) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            flag = False
            break
        else:
            flag = True
    ans.append(flag)

    # 세로
    flag = False
    col = []
    for i in range(9):
        for j in range(9):
            col.append(puzzle[j][i])
        if sorted(col) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            flag = False
            break
        else:
            flag = True
        col = []
    ans.append(flag)

    # 각 구역
    flag = False
    area = []
    for i in range(0, 7, 3):
        for j in range(0, 7, 3):
            for i2 in range(i, i + 3):
                for j2 in range(j, j + 3):
                    area.append(puzzle[i2][j2])
            if(sorted(area)) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                flag = False
                break
            else:
                flag = True
            area= []
    ans.append(flag)

    if 0 in ans:
        print('#{} 0'.format(t))
    else:
        print('#{} 1'.format(t))