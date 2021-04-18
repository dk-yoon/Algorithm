'''
-
'''
INF = int(1e9)

n = int(input())
graph = [[INF] * (1 + n) for _ in range(1 + n)]
ans = [[0] * (n) for _ in range(n)]
ans2 = []
min_num = 987654321
min_cnt = 0

for i in range(1, 1 + n):
    for j in range(1, 1 + n):
        if i == j:
            graph[i][j] = 0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    else:
        graph[a][b] = 1
        graph[b][a] = 1

for k in range(1, 1 + n):
    for a in range(1, 1 + n):
        for b in range(1, 1 + n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


for i in range(1, 1 + n):
    for j in range(1, 1 + n):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            ans[i-1][j-1] = (graph[i][j])

for an in ans:
    if min_num > max(an):
        min_num = max(an)

for i in range(n):
    if max(ans[i]) == min_num:
        ans2.append(i+1)

print(f'{min_num} {len(ans2)}')
print(*ans2)