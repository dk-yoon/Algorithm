grid = []
max_width = 19
plus_width = 2

for _ in range(plus_width):
    tmp = [0] * (max_width + 2 * plus_width)
    grid.append(tmp)

for _ in range(max_width):
    tmp = [0] * plus_width
    tmp.extend(list(map(int, input().split())))
    tmp.extend([0] * plus_width)
    grid.append(tmp)

for _ in range(plus_width):
    tmp = [0] * (max_width + 2 * plus_width)
    grid.append(tmp)

result = 0
total_width = plus_width + max_width
for i in range(plus_width,plus_width+max_width):
    for j in range(plus_width,plus_width+max_width):
        value = grid[i][j]

        if value: # value가 0인 아닌경우에만 확인 (흑색 또는 백색 돌)
            # 1 우향
            if value != grid[i][j - 1]:   # 이전 인덱스 (바로 왼쪽 돌) 와 다른 색 돌이 나왔을 경우
                for move in range(1,5):
                    if value != grid[i][j+move]:   # 다섯칸 우측까지 세어보고 다르면 멈춤
                        break
                else:
                    if value != grid[i][j+5]:   # 여섯번째 칸까지 육목 여부 확인 후 해당 돌 색과 인덱스 저장
                        result = (value, i, j)

            #2 우하향
            if value != grid[i - 1][j - 1]: # 좌측 상단 돌과 다른 색 돌이 나왔을 경우
                for move in range(1,5):
                    if value != grid[i+move][j+move]: # 우측 하단 대각선으로 다섯칸 오목여부를 확인
                        break
                else:
                    if value != grid[i+5][j+5]: # 여섯칸까지 육목 여부 확인 후 해당 돌 색과 인덱스 저장
                        result = (value, i,j)

            #3 하향
            if value != grid[i - 1][j]: # 바로 위 돌과 다른 색의 돌일 경우
                for move in range(1,5):
                    if value != grid[i+move][j]:   # 아래 쪽으로 다섯칸 오목여부 확인
                        break
                else:
                    if value != grid[i+5][j]:   # 육목 확인 후 돌 색과 인덱스 저장
                        result = (value, i, j)

            #4 좌하향
            if value != grid[i - 1][j + 1]: # 우상단 돌과 다른 색 돌이 나왔을 경우
                for move in range(1,5):
                    if value != grid[i+move][j-move]: # 좌측 하단 대각선으로 오목여부 확인
                        break
                else:
                    if value != grid[i+5][j-5]: #0,5 => 4,1
                        result = (value, i+4,j-4)   # 좌하향의 경우 가장 좌측 돌의 인덱스가 나와야하므로 가장 왼쪽 인덱스 저장

if result != 0:
    print("{}\n{} {}".format(result[0],result[1]-plus_width+1,result[2]- plus_width+1)) # 육목 및 이동확인을 위해 추가한 패딩 인덱스를 고려하여 계산
else:
    print(0)