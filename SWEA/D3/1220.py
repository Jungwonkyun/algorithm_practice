for tc in range(1, 11):
    N = int(input())
    sqaure = []
    for i in range(100):
        sqaure.append(list(map(str, input().split())))

    sqaure = list(map(list, zip(*sqaure)))
    result = 0

    # 1 == N 왼쪽 방향, 2 == S 오른쪽 방향
    for i in range(100):
        string = ""
        for j in range(100):
            if sqaure[i][j] != "0":
                string += sqaure[i][j]
        result += string.count("12")

    print("#{} {}".format(tc, result))
