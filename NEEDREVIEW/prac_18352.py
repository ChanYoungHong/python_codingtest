import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

q = deque([x]) # x = 1

while q:
    now = q.popleft()

    for next in graph[now]:
        if distance[next] == -1:
            distance[next] = distance[now] + 1
            q.append(next)

if k in distance:
    for i in range(1, n+1):
        if distance[i] == k:
            print(i)
else:
    print(-1)

