'''
BOJ1252. 이진수 덧셈
두 개의 이진수를 입력받아 이를 더하는 프로그램을 작성하시오.
'''

m, n = map(int, input().split())
add = list(str(m+n))
reversed = []
result = []

for i in add[::-1]:
    reversed.append(int(i))
reversed.append(0)

for j in range (0,len(reversed)):
    if reversed[j] > 1:
        reversed[j+1] += 1
        reversed[j] -= 2
for i in reversed[::-1]:
    result.append(str(i))

if result[0] == '0':
    del result[0]
print (''.join(result))
