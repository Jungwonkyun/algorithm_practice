test_case = int(input())
for n in range(1, test_case+1):
    score = [0]
    calorie = [0]
    N, L = map(int, input().split())
    DP = [[0]*10001 for _ in range(21)]
    for _ in range(N):
        t, k = map(int, input().split())
        score.append(t)
        calorie.append(k)

    for i in range(1, N+1):
        for j in range(1, L+1):
            if j < calorie[i]:
                DP[i][j] = DP[i-1][j]
            else:
                DP[i][j] = max(DP[i-1][j], DP[i-1][j-calorie[i]]+score[i])

    print("#{} {}".format(n, DP[N][L]))
