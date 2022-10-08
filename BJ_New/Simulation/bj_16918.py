from collections import deque

R, C, N = map(int, input().split())
rectangle = []
q = deque()


def bfs():

    global q

    # print(q)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while q:

        y, x = q.popleft()
        rectangle[y][x] = "."

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나지 않을 때
            if 0 <= nx < C and 0 <= ny < R:
                rectangle[ny][nx] = '.'

    return None


for i in range(R):
    rectangle.append(list(map(str, input())))

cnt = 0
check = True

for time in range(1, N):
    if time == 1:
        for y in range(R):
            for x in range(C):
                if rectangle[y][x] == "O":
                    q.append((y, x))
        rectangle = [["O"]*C for _ in range(R)]

    elif time != 1 and time % 2 != 0:
        for y in range(R):
            for x in range(C):
                if rectangle[y][x] == "O":
                    q.append((y, x))

        rectangle = [["O"]*C for _ in range(R)]

    elif time % 2 == 0:
        bfs()

for y in range(R):
    for x in range(C):
        print(rectangle[y][x], end="")
    print()
