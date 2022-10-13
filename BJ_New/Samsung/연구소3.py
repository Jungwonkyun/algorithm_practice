from collections import deque
from itertools import combinations as cm


def bfs(virus_list):
    dist = [[-1] * N for _ in range(N)]
    dq = deque()
    for pos in virus_list:
        dq.append(pos)
        dist[pos[0]][pos[1]] = 0
    max_dist = 0
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx = x+di[k][0]
            ny = y+di[k][1]

            if 0 <= nx < N and 0 <= ny < N and map_data[nx][ny] != 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y]+1
                if map_data[nx][ny] == 0:
                    max_dist = max(max_dist, dist[nx][ny])
                dq.append([nx, ny])

    a = list(sum(dist, []))
    if a.count(-1) == list(sum(map_data, [])).count(1):  # 방문 안 한 곳이 벽의 개수와 동일한지
        ans.append(max_dist)  # 리스트없이 바로 min값 구해도 됨


N, M = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(N)]
di = [[1, 0], [0, 1], [-1, 0], [0, -1]]

virus_pos = deque()
ans = []
for i in range(N):
    for j in range(N):
        if map_data[i][j] == 2:
            virus_pos.append([i, j])

for now_virus_list in cm(virus_pos, M):
    bfs(now_virus_list)

print(min(ans) if ans else -1)
