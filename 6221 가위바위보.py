p = str((input(["가위", "바위", "보"])))
q = str((input(["가위", "바위", "보"])))
if (p=="가위" and q=="바위")or(p=="바위" and q=="보")or(p=="보" and q=="가위"):
    print("Result: Man2 Win!")
elif (p=="가위" and q=="보")or(p=="바위" and q=="가위")or(p=="보" and q=="바위"):
    print("Result: Man1 Win!")
else:
    print("Result: Draw")

