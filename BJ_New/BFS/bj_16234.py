from collections import deque
import sys
sys.setrecursionlimit(10**5)


N, L, R = map(int, input().split())
country = []
country_queue = deque()
moving = 0


def bfs(y, x):

    global is_move
    country_queue.append((y, x))

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    people = country[y][x]
    cnt = 1
    memorization = [(y, x)]

    while country_queue:
        y, x = country_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
                # 인접국가와의 인구차이가 우리의 예상치 안일 때
                if L <= abs(country[y][x] - country[ny][nx]) <= R:
                    visited[ny][nx] = 1
                    country_queue.append((ny, nx))
                    people += country[ny][nx]
                    cnt += 1

                    # 인구 이동이 일어난 후 해당 좌표 사람수를 바꿔줘야함
                    memorization.append((ny, nx))

    # 인구이동후 사람수
    after = people//cnt

    if cnt > 1:
        is_move = True
        # 인구이동후 업데이트
        for index in memorization:
            y, x = index[0], index[1]
            country[y][x] = after

    return None


for i in range(N):
    country.append(list(map(int, input().split())))

while True:

    visited = [[0]*N for _ in range(N)]
    is_move = False

    # 각 좌표를 돌면서 visited가 아니면 그 지점에서 bfs를 돌린다.
    # 어디서 연합시 시작될지 모르니싸
    for y in range(N):
        for x in range(N):
            if visited[y][x] == 0:
                visited[y][x] = 1
                bfs(y, x)

    if is_move == True:
        moving += 1

    elif is_move == False:
        break

print(moving)
