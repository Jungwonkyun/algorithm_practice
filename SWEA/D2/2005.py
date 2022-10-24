test_case = int(input())

for n in range(test_case):
    N = int(input())
    triangle = [[0]*N for _ in range(N)]
    for i in range(N):
        triangle[i][0] = 1
        triangle[i][i] = 1

        if i >= 2:
            for k in range(1, i):
                triangle[i][k] = triangle[i-1][k-1] + triangle[i-1][k]

    print("#{}".format(n+1))
    print(1)
    for i in range(1, N):
        for j in range(0, i+1):
            print(triangle[i][j], end=" ")

        print()
