t = int(input())
for t in range (1,t+1):
    a, b = map(int, input().split())
    if a < b:
        print(f'#{t} <')
    elif a > b:
        print(f'#{t} >')
    else: print(f'#{t} =')