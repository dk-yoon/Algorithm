# 다음의 결과와 같이 어떤 한 양의 정수를 입력하여 그 숫자에 0~9가 몇 번 사용되었는지 표시하십시오.
n=int(input())
r=[0]*10
result = ""
while n:
    r[n%10] += 1
    n //= 10
for i in range(0,10):
    result += "%d " % i
print(result[0:len(result)-1])
result=""
for i in range(0,10):
    result += "%d " % r[i]
print(result[0:len(result)-1])