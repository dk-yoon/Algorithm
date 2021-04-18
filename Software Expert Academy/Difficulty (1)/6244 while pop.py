numbers = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
bb = 0
c = 0
while(len(numbers)):
    bb=int(numbers.pop())
    if(bb>=80):
        c+=bb
print(c)

