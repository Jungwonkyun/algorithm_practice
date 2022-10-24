test_case = int(input())

for n in range(test_case):
    N, M = map(int, input().split())
    room = []

    for _ in range(N):
        room.append(list(map(int, input().split())))

    maximum = 0

    for y in range(N-M+1):
        for x in range(N-M+1):
            total = 0
            start = room[y][x]
            for i in range(M):
                for j in range(M):
                    total += room[y+i][x+j]

            maximum = max(maximum, total)

    print("#{} {}".format(n+1, maximum))
