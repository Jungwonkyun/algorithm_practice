from collections import deque

N, M, K = map(int, input().split())
grid = []
dice = [1, 2, 3, 4, 5, 6]

# 방향은 시계 방향으로 동->남->서->북
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(y, x):

    visited = [[False]*M for _ in range(N)]
    dice_queue = deque()
    dice_queue.append((y, x))
    check = grid[y][x]
    cnt = 1

    while dice_queue:

        y, x = dice_queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if visited[ny][nx] == False and grid[ny][nx] == check:
                    dice_queue.append((ny, nx))
                    visited[ny][nx] = True
                    cnt += 1
            visited[y][x] = True

    return cnt


def roll(y, x, dir):

    score = 0
    # 주사위가 이동할 수 있는 횟수 만큼 반복
    for _ in range(K):
        # 다음 방향으로 이동할 수 없다면
        if not(0 <= x+dx[dir] < M and 0 <= y+dy[dir] < N):
            # 반대방향 회전
            dir = (dir+2) % 4

        # 다음 주사위가 이동할 좌표
        x = x+dx[dir]
        y = y+dy[dir]

        number = grid[y][x]

        count = bfs(y, x)
        score += number*count

        # dir방향대로 주사위 굴리기
        # 동쪽
        if dir == 0:
            dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]

        # 남쪽
        elif dir == 1:
            dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]

        # 서쪽
        elif dir == 2:
            dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]

        # 북쪽
        elif dir == 3:
            dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

        # 밑면이 더 크면 시계방향 회전
        if dice[5] > grid[y][x]:
            dir = (dir+1) % 4

        # 좌표가 더 크면 시계 반대방향 회전
        elif dice[5] < grid[y][x]:
            dir = (dir+3) % 4

    return score


for _ in range(N):
    grid.append(list(map(int, input().split())))


# (1,1)에서 dir 동쪽으로 solving 시작
print(roll(0, 0, 0))
