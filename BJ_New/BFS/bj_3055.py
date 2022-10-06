from collections import deque

M, N = map(int, input().split())
forest = []
water = []
start = []
end = []
animal_queue = deque()
visited = [[0]*N for _ in range(M)]


def bfs(y, x):

    cnt = 0
    animal_queue.append((y, x))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while animal_queue:
        # 물이 찰 예정인 칸은 가지 못하기 때문에 물을 미리 채운다
        for i in range(len(water)):
            wx = water[i][1]
            wy = water[i][0]

            for i in range(4):
                nx = wx+dx[i]
                ny = wy+dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    # 지금 지점이 *이고 다음 지점이 .일때 .을 *로 바꿔준다
                    if forest[ny][nx] == ".":
                        forest[ny][nx] = "*"
                        visited[ny][nx] = 1
                        water.append((ny, nx))

        # 물을 몇 번 채울 수 있는가
        cnt += 1

        for _ in range(len(animal_queue)):
            y, x = animal_queue.popleft()

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if 0 <= nx < N and 0 <= ny < M:
                    if forest[ny][nx] == ".":
                        if visited[ny][nx] == 0:
                            visited[ny][nx] = 1
                            animal_queue.append((ny, nx))

                    elif forest[ny][nx] == "D":
                        print(cnt)
                        # D에 도착하면 프린트하고 그냥 exit()으로 나가게 할 수도 있다
                        exit()

    return None


for i in range(M):
    forest.append(list(map(str, input())))

for y in range(M):
    for x in range(N):
        # 물, X, S 일때는 visited를 1로 줘서 탐색 안 하게 한다.
        if forest[y][x] == "*":
            water.append((y, x))
            visited[y][x] = 1

        elif forest[y][x] == "S":
            start.append((y, x))
            visited[y][x] = 1

        elif forest[y][x] == "X":
            end.append((y, x))
            visited[y][x] = 1

bfs(start[0][0], start[0][1])
print("KAKTUS")
