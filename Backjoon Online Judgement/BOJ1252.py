'''
BOJ1252. 이진수 덧셈
두 개의 이진수를 입력받아 이를 더하는 프로그램을 작성하시오.
'''
m, n = map(str, input().split())
m = '0b'+m
n = '0b'+n
m = int(m, 2)
n = int(n, 2)
result = bin(m+n)
print(result[2:])