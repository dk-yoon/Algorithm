def max(list):
    max = list[0]
    for i in range(1, len(list)):
        if list[i] > max:
            max = list[i]
    return max

def min(list):
    min = list[0]
    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]
    return min

T = 10
for t in range (1, 11):
    dump_count = int(input())
    box_list = list(map(int, input().split()))

    while True:
        box_list.append(max(box_list)-1)
        box_list.append(min(box_list)+1)
        box_list.remove(max(box_list))
        box_list.remove(min(box_list))
        dump_count -= 1
        if dump_count == 0:
            a = max(box_list)
            b = min(box_list)
            print(f'#{t} {a - b}')
            break