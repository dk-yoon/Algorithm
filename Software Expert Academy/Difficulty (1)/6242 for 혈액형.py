A = 0
B = 0
O = 0
AB = 0
type = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
for i in range(0,10):
    if type[i] == "A":
        A+=1
    elif type[i] == "B":
        B+=1
    elif type[i] == "O":
        O+=1
    else:
        AB+=1
print("{'A': "+str(A)+", 'O': "+str(O)+", 'B': "+str(B)+", 'AB': "+str(AB)+"}")
