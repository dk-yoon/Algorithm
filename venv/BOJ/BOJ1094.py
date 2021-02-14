'''
BOJ1094. 막대기 (수학, 비트마스킹)
X가 주어졌을 때, 위의 과정을 거친다면,
몇 개의 막대를 풀로 붙여서 Xcm를 만들 수 있는지 구하는 프로그램을 작성하시오.
'''
X = int(input())
X_bin = list(bin(X))
print(X_bin.count('1'))