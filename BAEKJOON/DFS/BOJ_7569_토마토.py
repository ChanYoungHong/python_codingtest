import sys
from collections import deque

input = sys.stdin.readline

'''
M : 가로
N : 세로
H : 높이

- 6방향으로 dfs을 돌려서 확인을 해야 함
'''

m, n, h = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[False] * m for _ in range(n)] for _ in range(h)]

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

answer = 0

q = deque()


def bfs():
    while q:

        x, y, z = q.popleft()

        for i in range(6):

            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
                if graph[nx][ny][nz] == 0 and visited[nx][ny][nz] == False:

                    q.append((nx, ny, nz))
                    graph[nx][ny][nz] = graph[x][y][z] + 1
                    visited[nx][ny][nz] = True


for a in range(h):
    for b in range(n):
        for c in range(m):

            if graph[a][b][c] == 1 and visited[a][b][c] == False:
                q.append((a, b, c))
                visited[a][b][c] = True

bfs()

for a in graph:
    for b in a:
        for c in b:

            if c == 0:
                print(-1)
                exit(0)

        answer = max(answer, max(b))

print(answer - 1)
