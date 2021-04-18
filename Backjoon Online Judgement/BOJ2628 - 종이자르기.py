'''
BOJ2628 - 종이자르기 (정렬)
'''

width, height = map(int, input().split())
paper = [[0] * width for _ in range(height)]
len_line = int(input())
line_list = []
width_point = []
height_point = []
width_gap = []
height_gap = []

for _ in range(len_line):
    n, point = map(int, input().split())
    if n == 0:
        height_point.append(point)  # 가로선에 해당하는 0은 height를 구분
    else:
        width_point.append(point)  # 세로선에 해당하는 1은 width를 구분

height_point.append(0)      # 양 끝 단인 0과 최대값을 포인트로 추가
height_point.append(height)
width_point.append(0)
width_point.append(width)
height_point.sort() # 인접 포인트 간의 차이를 계산하기 위해 sort 시행
width_point.sort()

for i in range(len(width_point)-1):
    width_gap.append(width_point[i+1] - width_point[i])     # 인접 포인트 간의 차이 계산
for j in range(len(height_point)-1):
    height_gap.append(height_point[j+1] - height_point[j])

print(max(width_gap) * max(height_gap))  # 최대 가로길이 * 최대 세로길이를 통해 최대 넓이 계산