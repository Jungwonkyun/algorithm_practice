N = int(input())
classroom = [[0]*N for _ in range(N)]
student = []
like = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def first(like):

    first_result = []
    check = False
    num = [[] * N for _ in range(N)]
    maximum = -1

    for y in range(N):
        for x in range(N):

            count = 0
            empty = 0

            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]

                # 범위 안에 있고 체크하는 칸에 좋아하는 학생이 있으면
                if 0 <= nx < N and 0 <= ny < N:
                    # 이미 학생이 없는 경우에만 더해준다
                    if classroom[ny][nx] in like and classroom[y][x] == 0:
                        count += 1

                    if classroom[ny][nx] == 0:
                        empty += 1

            num[y].append([count, empty])
            maximum = max(maximum, num[y][x][0])

    # print(num)

    for y in range(N):
        for x in range(N):
            if num[y][x][0] == maximum:
                first_result.append((y, x, num[y][x][1]))

    if len(first_result) == 1:
        check = True

    return first_result, check


for i in range(N**2):
    s, a, b, c, d = map(int, input().split())
    student.append(s)
    like.append([a, b, c, d])


for i in range(len(student)):
    now_student = student[i]
    likey = like[i]

    sit, check = first(likey)

    if check == True:
        classroom[sit[0][0]][sit[0][1]] = now_student
        continue

    else:
        second_result = []
        maximum = -1
        for i in range(len(sit)):
            maximum = max(maximum, sit[i][2])

        for i in range(len(sit)):
            if sit[i][2] == maximum:
                second_result.append((sit[i][0], sit[i][1]))

        if len(second_result) == 1:
            classroom[second_result[0][0]][second_result[0][1]] = now_student
            continue

        else:
            classroom[second_result[0][0]][second_result[0][1]] = now_student

result = 0
for y in range(N):
    for x in range(N):
        temp = 0
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]

            if 0 <= ny < N and 0 <= nx < N and classroom[ny][nx] and classroom[y][x] != 0:
                k = student.index(classroom[y][x])

                if classroom[ny][nx] in like[k]:
                    temp += 1

        if temp != 0:
            result += 10**(temp-1)

print(result)
