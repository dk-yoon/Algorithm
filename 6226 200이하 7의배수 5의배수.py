p=[]
for i in range(1,201):
    if (i % 7 ==0) and (i % 5 !=0):
        p.append(i)
q=",".join(map(str, p))
print(q)