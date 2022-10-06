from collections import deque

M, N = map(int, input().split())
treasure = []
treasure_queue = deque()

def bfs(y, x):
    treasure_queue.append((y, x))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while treasure_queue:
        y, x = treasure_queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[ny][nx] == 0:
                # 최단거리 구하는 문제
                if treasure[ny][nx] == "L":
                    visited[ny][nx] = visited[y][x]+1
                    treasure_queue.append((ny, nx))

    maxi = -1
    for item in visited:
        temp = max(item)
        if maxi < temp:
            maxi = temp
    return maxi


for i in range(M):
    treasure.append(list(map(str, input())))

maximum_list = []
visited = [[0]*N for _ in range(M)]

for y in range(M):
    for x in range(N):
        # 모든 지점에서 부터 검사해야하니까
        if treasure[y][x] == "L":
            visited = [[0]*N for _ in range(M)]
            visited[y][x] = 1
            maximum_list.append(bfs(y, x))

print(max(maximum_list)-1)
