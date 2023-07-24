import sys
from collections import deque

input = sys.stdin.readline

'''

1. 알고리즘
2. 시간복잡도 - 
3. 배열 - board로 배열을 받기, 행은 n으로 받기

'''

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):

    q = deque()
    q.append((x,y))

    while q:

        x, y = q.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    board[nx][ny] = board[x][y] + 1
                    q.append((nx, ny))
    return board[-1][-1]


print(bfs(0,0))
