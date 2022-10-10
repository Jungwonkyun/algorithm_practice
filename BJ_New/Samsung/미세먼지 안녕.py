R, C, T = map(int, input().split())
room = []
conditioner = []

for i in range(R):
    room.append(list(map(int, input().split())))

# 공기청정기 위치
for i in range(R):
    if -1 in room[i]:
        conditioner.append((i, 0))


U_dx = [0, 1, 0, -1]
U_dy = [-1, 0, 1, 0]

D_dx = [0, 1, 0, -1]
D_dy = [1, 0, -1, 0]


def spread():

    temp = [[0]*C for _ in range(R)]

    for y in range(R):
        for x in range(C):
            # 이번 칸의 미세먼지가 있고 공기 청정기 위치가 아니면 spread
            if room[y][x] != 0 and room[y][x] != -1:
                cnt = 0
                plus = 0
                # 4방향에 대해서 확산 계산
                for i in range(4):
                    nx = x+U_dx[i]
                    ny = y+U_dy[i]
                    # 퍼질 구간이 격자 내부이고 공기청정기가 아닐 때 spread
                    if 0 <= nx < C and 0 <= ny < R and room[ny][nx] != -1:
                        cnt += 1
                        plus = room[y][x]//5
                        temp[ny][nx] += plus
                        temp[y][x] -= plus

    for y in range(R):
        for x in range(C):
            room[y][x] += temp[y][x]

    return None


def air_up():

    # 윗쪽 공기 청정기 좌표
    y, x = conditioner[0]
    ny, nx = y-1, x
    i = 0

    while True:
        nx = nx+U_dx[i]
        ny = ny+U_dy[i]

        # 다시 공기 청정기로 돌아오면
        if nx == x and ny == y:
            break

        # 범위 밖으로 나가면 전으로 되돌리고 방향회전
        if not (0 <= nx < C and 0 <= ny <= y):
            ny = ny-U_dy[i]
            nx = nx-U_dx[i]
            i += 1
            continue

        # 확산 범위안에 있다면 미세먼지 업데이트
        room[ny-U_dy[i]][nx-U_dx[i]] = room[ny][nx]
        room[ny][nx] = 0

    return None


def air_down():

    # 아래쪽 공기 청정기 좌표
    y, x = conditioner[1]
    ny, nx = y+1, x
    i = 0

    while True:
        nx = nx+D_dx[i]
        ny = ny+D_dy[i]

        # 다시 공기 청정기로 돌아오면
        if nx == x and ny == y:
            break

        # 범위 밖으로 나가면 전으로 되돌리고 방향회전
        if not (0 <= nx < C and y <= ny < R):
            ny = ny-D_dy[i]
            nx = nx-D_dx[i]
            i += 1
            continue

        # 확산 범위안에 있다면 미세먼지 업데이트
        room[ny-D_dy[i]][nx-D_dx[i]] = room[ny][nx]
        room[ny][nx] = 0

    return None


def operate():

    spread()
    air_up()
    air_down()

    return None


for _ in range(T):
    operate()

result = 0

for y in range(R):
    for x in range(C):
        if room[y][x] != -1:
            result += room[y][x]

print(result)
