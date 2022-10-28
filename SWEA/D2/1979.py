test_case = int(input())

for n in range(test_case):
    N, K = map(int, input().split())
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    result = 0

    # 가로검색
    for y in range(N):
        cnt = 0
        for x in range(N):
            if puzzle[y][x] == 1:
                cnt += 1

            # 제일 끝이거나 벽을 마주친다면
            if x == N-1 or puzzle[y][x] == 0:

                if cnt == K:
                    result += 1
                cnt = 0

    # 세로검색
    for x in range(N):
        cnt = 0
        for y in range(N):
            if puzzle[y][x] == 1:
                cnt += 1

            # 제일 끝이거나 벽을 마주친다면
            if y == N-1 or puzzle[y][x] == 0:
                if cnt == K:
                    result += 1
                cnt = 0

    print("#{} {}".format(n+1, result))
