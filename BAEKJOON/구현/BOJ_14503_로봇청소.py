import sys

input = sys.stdin.readline

'''
방향 0:북쪽, 1:동쪽, 2:남, 3:서 

3 3
1 1 0
1 1 1
1 0 1
1 1 1

'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while 1:

    # 청소가 안 되어 있을 때 청소하기, 현재위치 청소하기
    if board[x][y] == 0:
        board[x][y] = 2
        cnt += 1

    flag = False
    # 그 위치가 청소가 됐는지 표시하기 위함
    for i in range(1, 5):
        nx = x + dx[d - i]
        ny = y + dy[d - i]

        if 0 <= nx < n and 0 <= ny < m:

            # 다음 방향을 보기 위해서
            # 반시계 방향으로 90도 회전한다.
            if board[nx][ny] == 0:
                # board[nx][ny] = 2
                d = (d - i + 4) % 4
                x = nx
                y = ny
                flag = True
                break

            # 청소되지 않은 빈 칸이 있는 경우
            # 바라보는 기준 앞쪽 칸이 청소되지 않은 빈 칸의 경우 한 칸 전진

    if flag == False:

        nx = x - dx[d]
        ny = y - dy[d]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 1:
                break
            else:
                x = nx
                y = ny
        else:
            break

print(cnt)

    # 4칸 중 청소되지 않은 빈 칸이 없는 경우
    #

    # 뒤쪽 방향이 막혀있는 지확인
