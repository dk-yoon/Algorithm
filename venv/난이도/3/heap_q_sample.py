from heapq import heapify, heappush, heappop

data = [69, 10, 30, 2, 16, 8, 31, 22]

print(data)
Q = []
for val in data:
    heappush(Q, val)

while Q:
    print(heappop(Q))
# heapify(data)
# heappush(data, 25)
print(data)