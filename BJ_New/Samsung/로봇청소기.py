from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []


# 북 -> 0,동 -> 1, 남 -> 2, 서 -> 3
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def solve(y, x, d):

    robot_queue = deque()
    robot_queue.append((y, x, d))
    cnt = 1

    while robot_queue:
        y, x, d = robot_queue.popleft()

        # 4방향 탐색
        for _ in range(4):
            # 다음 방향
            d = (d+3) % 4
            nx = x+dx[d]
            ny = y+dy[d]

            # 청소를 할 수 있으면
            if 0 <= nx < M and 0 <= ny < N and room[ny][nx] == 0:
                robot_queue.append((ny, nx, d))
                room[ny][nx] = 2
                cnt += 1
                break

        # 네 방향 모두 움직일 수 없을 때
        if not robot_queue:
            nx = x-dx[d]
            ny = y-dy[d]

            # 후진했는데 뒤가 범위를 벗어나거나 벽일 때
            if not (0 <= nx < M and 0 <= ny < N) or room[ny][nx] == 1:
                print(cnt)
                break

            # 후진했는데 벽이 아니면 그 좌표를 다시 넣어준다
            else:
                robot_queue.append((ny, nx, d))

    return None


for i in range(N):
    room.append(list(map(int, input().split())))

room[r][c] = 2
solve(r, c, d)
