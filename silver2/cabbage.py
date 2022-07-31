# Code by 정원균
# BaekJoon #1012

import sys
sys.setrecursionlimit(10000)  # recursion error가 발생하면 다음 모듈 import 해줘야한다.

test_case = int(input())


def dfs(x, y, max_X, max_Y, graph):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if (0 <= nx < max_X and 0 <= ny < max_Y):
            if graph[ny][nx] == 1:
                graph[ny][nx] = -1
                dfs(nx, ny, max_X, max_Y, graph)


for i in range(test_case):

    loc_X, loc_Y, num_cabbage, = map(int, input().split())

    cabbage_map = [[0]*loc_X for _ in range(loc_Y)]
    cnt = 0

    for j in range(num_cabbage):

        x, y = map(int, input().split())
        cabbage_map[y][x] = 1

    for x in range(loc_X):
        for y in range(loc_Y):
            if cabbage_map[y][x] == 1:
                dfs(x, y, loc_X, loc_Y, cabbage_map)
                cnt += 1
    print(cnt)
