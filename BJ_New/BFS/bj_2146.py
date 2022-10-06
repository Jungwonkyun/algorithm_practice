from collections import deque

N = int(input())
mapping = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def minimum_bfs(cnt):

    global result
    # 기본 -1로 초기화 해주고 bfs를 시작할 포인트는 0으로 초기화 시켜준다.
    distance = [[-1]*N for _ in range(N)]
    map_queue = deque()
    for y in range(N):
        for x in range(N):
            if mapping[y][x] == cnt:
                map_queue.append((y, x))
                distance[y][x] = 0

    while map_queue:

        y, x = map_queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                # 새로운 땅을 만나고, 자기 땅이 아닐 경우
                if mapping[ny][nx] > 0 and mapping[ny][nx] != cnt:

                    result = min(distance[y][x], result)
                    return

                # 바다를 만났을 경우
                elif mapping[ny][nx] == 0 and distance[ny][nx] == -1:
                    # distance growing
                    distance[ny][nx] = distance[y][x]+1
                    map_queue.append((ny, nx))

    return None


def bfs(y, x):
    global cnt
    map_queue = deque()
    map_queue.append((y, x))
    mapping[y][x] = cnt

    while map_queue:
        y, x = map_queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < N and visited[ny][nx] == 0:
                if mapping[ny][nx] == 1:
                    visited[ny][nx] = 1
                    map_queue.append((ny, nx))

                    # 1번째 bfs에서 region labeling을 해줘서 자기 땅을 자기가 방문하지 않도록 한다.
                    mapping[ny][nx] = cnt

    return None


for i in range(N):
    mapping.append(list(map(int, input().split())))


visited = [[0]*N for _ in range(N)]
cnt = 0
for y in range(N):
    for x in range(N):
        if mapping[y][x] == 1 and visited[y][x] == 0:
            visited[y][x] = 1
            cnt += 1
            # 여기서 땅 하나씩 labeling
            bfs(y, x)

result = 100000000

for i in range(1, cnt+1):
    # 땅의 label 갯수에 따라서 각 땅에서 다른 땅까지의 최소거리 계산
    minimum_bfs(i)

print(result)
