N = int(input())
triangle = [[]]
DP = [[]for _ in range(N+1)]

for _ in range(N):
    triangle.append(list(map(int, input().split())))

for i in range(1, N+1):
    if i == 1:
        DP[1].append(triangle[1][0])
        continue

    elif i == 2:
        DP[2].append(triangle[1][0]+triangle[2][0])
        DP[2].append(triangle[1][0]+triangle[2][1])
        continue

    for j in range(i):
        if j == 0:
            DP[i].append(DP[i-1][0]+triangle[i][0])

        elif j == i-1:
            DP[i].append(DP[i-1][-1]+triangle[i][-1])

        else:
            DP[i].append(max(DP[i-1][j-1], DP[i-1][j])+triangle[i][j])


print(max(DP[N]))
