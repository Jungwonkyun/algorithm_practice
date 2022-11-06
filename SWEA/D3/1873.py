test_case = int(input())
control_dict = {"U": 0, "R": 1, "D": 2, "L": 3}
tank_dir = {"U": "^", "R": ">", "D": "v", "L": "<"}
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

for t in range(1, test_case+1):
    H, W = map(int, input().split())
    mapping = []
    for _ in range(H):
        mapping.append(list(map(str, input())))

    INPUT = int(input())
    control = list(map(str, input()))

    s_y, s_x = 0, 0
    direction = 0
    for y in range(H):
        for x in range(W):
            if mapping[y][x] == "^":
                direction = 0
                s_y, s_x = y, x
                break

            elif mapping[y][x] == ">":
                direction = 1
                s_y, s_x = y, x
                break

            elif mapping[y][x] == "v":
                direction = 2
                s_y, s_x = y, x
                break

            elif mapping[y][x] == "<":
                direction = 3
                s_y, s_x = y, x
                break

    d = 0
    for i in range(len(control)):

        if i == 0 and control[i] == "S":
            d = direction

        elif i != 0 and control[i] == "S":
            pass

        else:
            d = control_dict[control[i]]

        ny = s_y + dy[d]
        nx = s_x + dx[d]

        # 탱크 방향 바꾸기
        if control[i] != "S":
            mapping[s_y][s_x] = tank_dir[control[i]]

        if control[i] == "S":
            while True:
                # 맵 밖으로 벗어나는 경우
                if not (0 <= ny < H and 0 <= nx < W):
                    break
                # 평지나 물을 만나면 계속 직진
                elif mapping[ny][nx] == "." or mapping[ny][nx] == "-":
                    ny = ny + dy[d]
                    nx = nx + dx[d]
                    continue
                # 벽돌인 벽을 만나면
                elif mapping[ny][nx] == "*":
                    mapping[ny][nx] = "."
                    break
                # 강철로 된 벽을 만나면
                else:
                    break

        # 범위 안에 있고 다음이 평지이며 이동 시그널 일때는
        elif (0 <= ny < H and 0 <= nx < W) and mapping[ny][nx] == "." and control[i] != "S":
            # 탱크는 이동 + 방향전환, 원래 위치는 평지가 된다.
            if mapping[ny][nx] == ".":
                mapping[ny][nx] = tank_dir[control[i]]
                mapping[s_y][s_x] = "."
                s_y, s_x = ny, nx

    print("#{}".format(t), end=" ")
    for y in range(H):
        for x in range(W):
            print(mapping[y][x], end="")
        print()
