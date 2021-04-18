p = []
for i in range (1,101):
    if i % 2 == 1 :
        p.append(i)
q=", ".join(map(str, p))
print(q)