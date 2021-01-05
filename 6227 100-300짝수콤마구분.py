p=[]
for i in range(100,301):
    if (i // 100 == 2) and (i % 20 <= 9) and (i % 2 == 0):
        p.append(i)
q=",".join(map(str, p))
print(q)