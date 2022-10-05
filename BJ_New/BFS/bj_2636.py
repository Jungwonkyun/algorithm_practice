from collections import deque

M, N = map(int, input().split())
cheeze = []
cheeze_queue = deque()
end = False


def bfs(y, x):

    global end
    cheeze_queue.append((y, x))
    outer_cheeze = []

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while cheeze_queue:
        y, x = cheeze_queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < N and 0 <= ny < M and visited[ny][nx] == 0:
                visited[ny][nx] = 1

                # 바깥 공간이면 deque에 넣고 계속 bfs돌린다
                if cheeze[ny][nx] == 0:
                    cheeze_queue.append((ny, nx))

                # 치즈가 있으면 queue에 넣지 않고 나중에 바꿔줘야 하니까 list에 저장해둔다.
                elif cheeze[ny][nx] == 1:
                    outer_cheeze.append((ny, nx))

    # 공기와 접촉해있는 치즈를 없애준다
    for y, x in outer_cheeze:
        cheeze[y][x] = 0

    temp = 0

    # 치즈가 녹고난 후 남은 치즈 계산
    for y in range(M):
        for x in range(N):
            if cheeze[y][x] == 1:
                temp += 1

    if temp == 0:
        end = True

    return len(outer_cheeze)


for i in range(M):
    cheeze.append(list(map(int, input().split())))

cnt = 0
num_cheeze = 0

while True:
    visited = [[0]*N for _ in range(M)]
    num_cheeze = bfs(0, 0)
    cnt += 1

    if end == True:
        break

print(cnt)
print(num_cheeze)
