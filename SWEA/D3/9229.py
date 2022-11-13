TC = int(input())

for t in range(1, TC+1):
    N, M = map(int, input().split())
    snack = list(map(int, input().split()))
    result = -1
    for i in range(len(snack)-1):
        if snack[i] >= M:
            continue
        for j in range(len(snack)):
            if snack[i]+snack[j] <= M:
                result = max(result, snack[i]+snack[j])
    print("#{} {}".format(t, result))
