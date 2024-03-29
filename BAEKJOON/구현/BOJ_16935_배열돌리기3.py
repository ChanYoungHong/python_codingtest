import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
board = [list(map(int, input().rstrip().split())) for _ in range(n)]
num = list(map(int, input().rstrip().split()))

for i in range(r):  # 0 1 2 3 4 5

    # if num[i] == 1:
    #     for j in range(n - 1, -1, -1):
    #         for k in range(m):
    #             print(board[j][k], end=' ')
    #         print()
    #
    # elif num[i] == 2:
    #     for j in range(n):
    #         for k in range(m - 1, -1, -1):
    #             print(board[j][k], end=' ')
    #         print()

    if num[i] == 1:
        length = len(board)
        for j in range(6):
            board[j], board[length - 1 - j] = board[length - 1 - j], board[j]
            print('board[j] : ', board[j])
            print('board[length - 1 - j] : ', board[length - 1 - j])

    elif num[i] == 2:
        for i in range(len(board)):  # 0 1 2 3 4 5
            board[i] = list(reversed(board[i]))
            # print('board[i] : ', board[i])

    # elif num[i] == 3:

    # temp = []
    # # x는 올라감, y는 내려감 -> 가로에서 세로가 될 때
    # for j in range(n):
    #     for k in range(m):
    #
    #         if board[j][k]:
    #
    # # 세로에서 가로 될 때 -> x는 내려감, y도 올라감
    # for z in range():
    #     for x in range():

    elif num[i] == 3:
        if len(board) == n:
            new_board = [[0] * n for _ in range(m)]
            for j in range(m):  # 0 1 2 3 4 5 6 7
                for k in range(n):  # 0 1 2 3 4 5
                    new_board[j][n - 1 - k] = board[k][j]
                    print('new_board[j][n-1-k] : ', j, n - 1 - k)
                    print('board[k][j] : ', k, j)
        else:
            new_board = [[0] * m for _ in range(n)]
            for j in range(n): # 0 1 2 3 4 5
                for k in range(m):# 0 1 2 3 4 5 6 7
                    new_board[j][m - 1 - k] = board[k][j]
        board = new_board

    elif num[i] == 4:
        if len(board) == n:
            new_board = [[0] * n for _ in range(m)]
            for j in range(m - 1, -1, -1):
                for k in range(n - 1, -1, -1):
                    new_board[(m - 1) - j][k] = board[k][j]
        else:
            new_board = [[0] * m for _ in range(n)]
            for j in range(n - 1, -1, -1):
                for k in range(m - 1, -1, -1):
                    new_board[(n - 1) - j][k] = board[k][j]

        board = new_board

    elif num[i] == 5:
        r, c = len(board), len(board[0])
        new_board = [[0] * c for _ in range(r)]

        arr1 = [item[:c // 2] for item in board[:r // 2]]
        arr2 = [item[c // 2:] for item in board[:r // 2]]
        arr3 = [item[c // 2:] for item in board[r // 2:]]
        arr4 = [item[:c // 2] for item in board[r // 2:]]

        for j in range(r // 2):
            new_board[j] = arr4[j] + arr1[j]

        for j in range(r // 2, r):
            new_board[j] = arr3[j - r // 2] + arr2[j - r // 2]
        board = new_board

    elif num[i] == 6:

        # 1 -> 4 -> 3 -> 2 -> 1
        r, c = len(board), len(board[0])
        new_board = [[0] * c for _ in range(r)]

        arr1 = [item[:c // 2] for item in board[:r // 2]]
        arr2 = [item[c // 2:] for item in board[:r // 2]]
        # item[4:] 4 5 6 7                      board[3:] 3 4 5
        arr3 = [item[c // 2:] for item in board[r // 2:]]
        arr4 = [item[:c // 2] for item in board[r // 2:]]

        print('arr1 : ', arr1)
        print('arr2 : ', arr2)
        print('arr3 : ', arr3)
        print('arr4 : ', arr4)

        for j in range(r // 2): # 0 1 2
            new_board[j] = arr2[j] + arr3[j]
            print('arr2[j]', arr2[j])
            print('arr3[j]', arr3[j])
            print('new_board[j]', new_board[j])

        for j in range(r // 2, r): # 3 4 5
            new_board[j] = arr1[j - r // 2] + arr4[j - r // 2]
        board = new_board

for arr in board:
    print(*arr)
