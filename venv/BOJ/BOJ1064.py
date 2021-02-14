'''
BOJ1064. 평행사변형 (기하학)
'''
# 두변 길이의합 * 2
def hypo(a, b):
    c = (a ** 2 + b ** 2) ** 0.5
    return c

x1, y1, x2, y2, x3, y3 = map(int, input().split())

# 오른쪽 + 위쪽 +
range1 = hypo((x2 - x1), (y2 - y1))
range2 = hypo((x3 - x1), (y3 - y1))
answer1 = (range1 + range2) * 2

# 오른쪽 + 위쪽 -
range3 = hypo((x3 - x2), (y3 - y2))
range4 = hypo((x2 - x1), (y2 - y1))
answer2 = (range3 + range4) * 2

# 오른쪽 - 위쪽 +
range5 = hypo((x3 - x2), (y3 - y2))
range6 = hypo((x3 - x1), (y3 - y1))
answer3 = (range5 + range6) * 2

# 예외처리 (기울기 : y증가량 /  x증가량이 서로 같을 때) - 제로디비전 오류 떠서 곱으로 함

if (x2-x1)*(y3-y1) == (y2-y1)*(x3-x1):
    print(-1)
else:
    print(max(answer1, answer2, answer3) - min(answer1, answer2, answer3))