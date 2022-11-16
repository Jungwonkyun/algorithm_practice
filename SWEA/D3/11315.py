test_case = int(input())
dx = [1, 0, -1, 1]
dy = [0, 1, 1, 1]


for tc in range(1, test_case+1):
    N = int(input())
    board = []
    flag = "NO"
    for _ in range(N):
        board.append(list(map(str, input())))

    for y in range(N):
        for x in range(N):
            if board[y][x] == "o":
                for i in range(4):
                    nx = x
                    ny = y
                    cnt = 1
                    while 0 <= nx+dx[i] < N and 0 <= ny+dy[i] < N:
                        nx = nx+dx[i]
                        ny = ny+dy[i]
                        if board[ny][nx] == "o":
                            cnt += 1

                        elif board[ny][nx] == ".":
                            if cnt == 5:
                                flag = "YES"
                                break
                            else:
                                break
                        if cnt == 5:
                            flag = "YES"
                            break
                    if flag == "YES":
                        break
            if flag == "YES":
                break
        if flag == "YES":
            break

    print("#{} {}".format(tc, flag))
