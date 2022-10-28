test_case = int(input())

for n in range(test_case):
    N = int(input())
    num_list = []
    result = [["0"]*3 for _ in range(N)]
    for _ in range(N):
        num_list.append(list(map(int, input().split())))

    for i in range(3):
        rotate = [[0]*N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                rotate[x][N-1-y] = num_list[y][x]
        num_list = rotate

        for j in range(N):
            temp = ""
            for k in range(N):
                temp += str(num_list[j][k])
            result[j][i] = temp

    print("#{}".format(n+1))
    for i in range(N):
        for j in range(3):
            print(result[i][j], end=" ")
        print()
