import sys

input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y):

    global cnt
    cnt += 1

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1:
                board[nx][ny] = 0
                dfs(nx,ny)

    return cnt
cnt = 0

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]

res = []
for i in range(n):
    for j in range(n):

        if board[i][j] == 1:
            board[i][j] = 0
            res.append(dfs(i,j))
            cnt = 0

print(len(res))
res.sort()
for i in res:
    print(i+1)