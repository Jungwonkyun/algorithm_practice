from collections import deque
import itertools
import copy

N, M = map(int, input().split())
lab = []
lab_list = []
virus_list = []
lab_queue = deque()


def bfs():

    visited = [[0]*M for _ in range(N)]

    for virus in virus_list:
        lab_queue.append(virus)

    cnt = 0

    # 기본 틀은 DFS와 비슷하다
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while lab_queue:
        y, x = lab_queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if visited[ny][nx] == 0 and lab[ny][nx] == 0:
                    visited[ny][nx] = 1
                    lab_queue.append((ny, nx))
                    cnt += 1

    # 전체 0의 갯수에서 바이러스가 퍼저나간 부분 제외 + 벽3개 세운거 제외가 최대가 되어야 한다.
    return len(lab_list)-cnt-3


for i in range(N):
    lab.append(list(map(int, input().split())))

for y in range(N):
    for x in range(M):
        # 연구소 빈공간 좌표
        if lab[y][x] == 0:
            lab_list.append((y, x))

        # 바이러스 좌표
        if lab[y][x] == 2:
            virus_list.append((y, x))

# 연구소 남은 공간 중에서 3개를 조합으로 선택해서 리스트로 저장
nCr = list(itertools.combinations(lab_list, 3))

maximum = 0

for ncr in nCr:
    # 3개의 벽을 세운다 nCr로 뽑은 것들 중에
    lab[ncr[0][0]][ncr[0][1]] = 1
    lab[ncr[1][0]][ncr[1][1]] = 1
    lab[ncr[2][0]][ncr[2][1]] = 1

    temp = bfs()
    if maximum < temp:
        maximum = temp

    # 벽 세운거 다시 복구
    lab[ncr[0][0]][ncr[0][1]] = 0
    lab[ncr[1][0]][ncr[1][1]] = 0
    lab[ncr[2][0]][ncr[2][1]] = 0

print(maximum)
