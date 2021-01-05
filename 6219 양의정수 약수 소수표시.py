number1 = int(input())
number2 = 0
for i in range(1,number1+1):
    if number1 % i ==0:
        print("%d(은)는 %d의 약수입니다." %(i,number1))
        number2 = number2 + i
if number2 == (number1 + 1):
    print("%d(은)는 1과 %d로만 나눌 수 있는 소수입니다." %(i,i))
