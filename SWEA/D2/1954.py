from collections import deque

test_case = int(input())

for n in range(test_case):
    N = int(input())
    # 기본값 초기화
    snail = [[0]*N for _ in range(N)]

    # 동 -> 남 -> 서 -> 북 방향으로 반복된다
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    plus_queue = deque()
    plus_queue.append((0, 0))

    pivot = 0
    snail[0][0] = 1
    cnt = 0
    while cnt < N**2-1:

        y, x = plus_queue.popleft()
        nx = x + dx[pivot]
        ny = y + dy[pivot]

        # snail 숫자를 더해준다
        if 0 <= nx < N and 0 <= ny < N and snail[ny][nx] == 0:
            snail[ny][nx] = snail[y][x]+1
            plus_queue.append((ny, nx))
            cnt += 1
            

        # 범위를 벗어나거나 이미 값이 있는 칸을 만나면
        else:
            plus_queue.append((y, x))
            pivot = (pivot+1) % 4

    
    print("#{}".format(n+1))

    for y in range(N):
        for x in range(N):
            print(snail[y][x], end=" ")
        print()
