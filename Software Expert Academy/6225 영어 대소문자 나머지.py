p = str((input()))
lowp = p.lower()
upp = p.upper()
asc1 = ord(lowp)
asc2 = ord(upp)

if p == upp:
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(p,asc2,lowp,asc1))
elif p == lowp:
    print("%s(ASCII: %d) => %s(ASCII: %d)" %(p,asc1,upp,asc2))
else:
    print(p)