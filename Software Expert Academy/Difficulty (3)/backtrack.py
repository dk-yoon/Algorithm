N = 5
choice = [0] * 3
def backtrack(idx, row_sum):
    if row_sum > N: return
    if idx == 3:
        if row_sum == 5:
            print(row_sum, '-->', choice)
    else:
        for i in range(1, N - 2 + 1):
            choice[idx] = i
            backtrack(idx + 1, row_sum + i)

backtrack(0, 0)