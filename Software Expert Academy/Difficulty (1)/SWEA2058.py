'''
하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
'''
n = (input())

if int(n) < 10 :
    first = int(n[0:1])
    print(first)
elif int(n) >= 10 and int(n) < 100 :
    first = int(n[0:1])
    second = int(n[1:2])
    print(first + second)
elif int(n) >= 100 and int(n) < 1000 :
    first = int(n[0:1])
    second = int(n[1:2])
    third = int(n[2:3])
    print(first + second + third)
else:
    first = int(n[0:1])
    second = int(n[1:2])
    third = int(n[2:3])
    fourth = int(n[3:4])
    print(first+second+third+fourth)