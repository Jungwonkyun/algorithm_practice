test_case = int(input())

# 대각선 4개, 상하좌우
dx = [-1, 1, 1, -1, 0, 0, -1, 1]
dy = [-1, -1, 1, 1, 1, -1, 0, 0]

for t in range(1, test_case+1):
    N, M = map(int, input().split())
    board = [[0]*N for _ in range(N)]
    board[N//2-1][N//2-1] = 2
    board[N//2][N//2] = 2
    board[N//2][N//2-1] = 1
    board[N//2-1][N//2] = 1

    for n in range(M):
        y, x, r = map(int, input().split())
        y -= 1
        x -= 1
        if board[y][x] == 0:
            board[y][x] = r
            for i in range(8):
                nx = x+dx[i]
                ny = y+dy[i]
                # reverse는 뒤집어줄 위치 리스트
                reverse = []
                while True:
                    # 탐색중에 칸을 벗어나는 경우 이 방향으론 바꿀 색깔 x
                    if 0 > nx or nx >= N or 0 > ny or ny >= N:
                        reverse = []
                        break
                    # 다음 만난 게 빈칸일 때 이 방향으론 바꿀 색깔 x
                    if board[ny][nx] == 0:
                        reverse = []
                        break
                    # 다음 자기랑 같은 색깔을 만날 때 일단 계속 탐색
                    if board[ny][nx] == r:
                        break
                    else:
                        reverse.append((ny, nx))
                    nx += dx[i]
                    ny += dy[i]
                    # 다른 방향 탐색전에 이 탐색방향에 해당하는 돌들 바꿔주기

                for ry, rx in reverse:
                    board[ry][rx] = r
    w, b = 0, 0
    for y in range(N):
        for x in range(N):
            if board[y][x] == 1:
                b += 1
            elif board[y][x] == 2:
                w += 1
    print("#{} {} {}".format(t, b, w))
