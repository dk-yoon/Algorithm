arr = 'ABCDE'
N = len(arr)
R = 3
for i in range(0, N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            print(arr[i], arr[j], arr[k])
print('-' * 10)
#-----------------------------------------
choice = [0] * R
def comb(idx, start):
    if idx == R:
        print(choice)
    else:
        for i in range(start, N):
            choice[idx] = arr[i]
            comb(idx + 1, i + 1)
comb(0, 0)