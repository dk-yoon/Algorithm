T = int(input())
for t in range(1, T + 1):
    tc, N = map(str, input().split())
    N = int(N)
    num1_list = list(map(str, input().split()))
    num2_list = []

    # "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
    for number in num1_list:
        if number == "ZRO":
            num2_list.append(0)
        elif number == "ONE":
            num2_list.append(1)
        elif number == "TWO":
            num2_list.append(2)
        elif number == "THR":
            num2_list.append(3)
        elif number == "FOR":
            num2_list.append(4)
        elif number == "FIV":
            num2_list.append(5)
        elif number == "SIX":
            num2_list.append(6)
        elif number == "SVN":
            num2_list.append(7)
        elif number == "EGT":
            num2_list.append(8)
        elif number == "NIN":
            num2_list.append(9)
        num2_list.sort()
    print(num2_list[num2_list.index(0)])
    print(tc)
    print(" ".join(num2_list))