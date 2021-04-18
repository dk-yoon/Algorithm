data = [69, 10, 30, 2, 16, 8, 31, 22]

H = [0] * 100
hsize = 0

def push(item):
    global hsize
    hsize += 1
    H[hsize] = item
    c = hsize   # 자식
    p = hsize // 2  # 부모
    
    while p:    # p가 0이 아닐동안 반복
        if H[p] < H[c]: # 자식이 부모보다 클 때
            H[p], H[c] = H[c], H[p] # 두 위치를 변경
            c = p
            p = c // 2
        else:
            break

def pop():
    global hsize
    ret = H[1]
    H[1] = H[hsize]
    hsize -= 1
    p = 1   # 부모
    c = p * 2   # 왼쪽 자식

    while c <= hsize:
        if c + 1 <= hsize and H[c] < H[c+1]: #오른쪽 자식이 범위 안에 있고 오른쪽 자식이 클 때
            c += 1  # 오른쪽을 가리키게
        if H[p] < H[c]:
            H[p], H[c] = H[c], H[p] # 바꿀 필요가 있으면 바꾸고
            p = c   # 다시 부모와 자식을 선택
            c = p * 2
        else:
            break
            
    return ret

for val in data:
    push(val)

while hsize:
    print(pop(), end = ' ')