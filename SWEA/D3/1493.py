test_case = int(input())

board = [[-1]*300 for _ in range(300)]
board[0][0] = 1
cnt = 2
for i in range(1, 300):
    board[0][i] = board[0][i-1]+cnt
    cnt += 1

for i in range(1, 300):
    for j in range(0, 299):
        board[i][j] = board[i-1][j+1]-1

for tc in range(1, test_case+1):
    P, Q = map(int, input().split())
    a, b, c, d = 0, 0, 0, 0

    for y in range(len(board)):
        if P in board[y]:
            a = board[y].index(P)+1
            b = y+1

        if Q in board[y]:
            c = board[y].index(Q)+1
            d = y+1

        if a != 0 and b != 0 and c != 0 and d != 0:
            break

    r1, r2 = a+c, b+d

    print("#{} {}".format(tc, board[r2-1][r1-1]))
