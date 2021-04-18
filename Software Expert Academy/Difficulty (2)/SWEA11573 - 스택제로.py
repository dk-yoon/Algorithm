def push(item):
    stack.append(item)

def pop():
    return stack.pop()

def isEmpty():
    return len(stack) == 0



    stack_sum = 0
    items = list(map(int, input().split()))

    for item in items:
        if item == 0:
            pop()
        else:
            push(item)

    for stk in stack:
        stack_sum += stk
    print('#{} {}'.format(t, stack_sum))