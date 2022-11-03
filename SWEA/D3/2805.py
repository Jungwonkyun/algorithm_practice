test_case = int(input())

for t in range(1, test_case+1):
    N = int(input())
    ground = []
    for _ in range(N):
        temp = list(map(int, input()))
        ground.append(temp)

    mid = N//2
    s = mid
    e = mid
    result = 0

    for y in range(N):
        for x in range(s, e+1):
            result += ground[y][x]
        if y < mid:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print("#{} {}".format(t, result))
