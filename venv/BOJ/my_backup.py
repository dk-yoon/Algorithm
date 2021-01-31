
T = int(input())
two = [2, 4, 8, 6]
three = [3, 9, 7, 1]
four = [4, 6]
seven = [7, 9, 3, 1]
eight = [8, 4, 2, 6]
nine = [9, 1]

for t in range (T):
    a, b = map(int,input().split())
    a = a % 10
    four_count = b % 4
    if a == 0:
        answer = 10
    elif a == 1:
        answer = 1
    elif a == 2 and b >= 2:
        answer = two[four_count - 1]
    elif a == 3 and b >= 2:
        answer = three[four_count - 1]
    elif a == 4:
        if b % 2: answer = 4
        else: answer = 6
    elif a == 5:
        answer = 5
    elif a == 6:
        answer = 6
    elif a == 7 and b >= 2:
        answer = seven[four_count - 1]
    elif a == 8 and b >= 2:
        answer = eight[four_count - 1]
    elif a == 9:
        if b % 2: answer = 9
        else: answer = 1
    elif b == 0:
        answer = 1
    print (answer)