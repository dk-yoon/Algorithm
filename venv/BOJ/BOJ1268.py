'''
BOJ1268. 임시 반장 정하기 (분류, 구현)
각 학생들이 1학년부터 5학년까지 속했던 반이 주어질 때, 임시 반장을 정하는 프로그램을 작성하시오.
'''
students = []
T = int(input())
count= [0] * T
students = []
all = [[set() for _ in range(10)] for _ in range(5)] # 9개까지의 반, 5개까지의 학년

for i in range(T):
    students.append(list(map(int, input().split())))
    for j in range(5):
        all[j][students[i][j]].add(i)

for i in range(T):
    check = set()
    for j in range(5):
        check |= all[j][students[i][j]]
    count[i] = len(check)

print(count.index(max(count)) + 1)