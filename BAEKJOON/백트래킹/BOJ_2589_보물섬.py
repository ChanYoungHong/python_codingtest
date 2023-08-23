import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(i,j):

    q = deque()
    q.append((i,j))

    visited = [[0] * m for _ in range(n)]
    visited[i][j] = 1
    cnt = 0

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx,ny))

    return cnt - 1


result = 0
for i in range(n):
    for j in range(m):

        if board[i][j] == 'L':
            result = max(result, bfs(i,j))

print(result)
