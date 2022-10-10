N = int(input())
curve = []

# 순서는 동->북->서->남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
visited = [[False]*102 for _ in range(102)]


def make_curve(y, x, di, g):

    curve_list = [di]

    # 세대에 따른 curve_list 생성
    for _ in range(g):
        temp = list(reversed(curve_list))
        for j in range(len(temp)):
            temp[j] = (temp[j]+1) % 4
        curve_list += temp

    # 시작 좌표 방문 표시해주고
    visited[y][x] = True

    nx, ny = x, y

    for d in curve_list:
        nx = nx+dx[d]
        ny = ny+dy[d]
        if visited[ny][nx] == False:
            visited[ny][nx] = True

    return None


for i in range(N):
    x, y, d, g = map(int, input().split())
    curve.append((y, x, d, g))

for item in curve:
    y, x, d, g = item
    make_curve(y, x, d, g)

rectangle = 0

for y in range(102):
    for x in range(102):
        #print(y, x,visited[y][x])
        if visited[y][x] == True:
            # print(y,x)
            ny, nx = y, x
            if 0 <= nx < 102 and 0 <= ny < 102:
                if visited[y+1][x] == 1 and visited[y][x+1] == 1 and visited[y+1][x+1] == 1:
                    rectangle += 1

print(rectangle)
