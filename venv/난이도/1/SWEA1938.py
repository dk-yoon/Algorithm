'''
두 개의 자연수를 입력받아 사칙연산을 수행하는 프로그램을 작성하라.
'''
a, b = map(int, input().split())
add = a + b
sub = a - b
mul = a * b
div = int(a / b)
print(add)
print(sub)
print(mul)
print(div)