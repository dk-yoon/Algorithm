'''
BOJ15652 - N과 M (4) (백트래킹)
'''
n, m = map(int,input().split())
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
k = [0 for _ in range(m)] # 출력 개수

def dfs(idx,next):
    if idx >= m: # 0부터 m출력개수 되면
        print(*k)
        return
    for i in range(next,n):
        k[idx] = numbers[i]
        dfs(idx+1,i) # 재귀포문에선 처음부터 아닌 나부터~
dfs(0,0)