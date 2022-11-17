test_case = int(input())

for tc in range(1, test_case+1):
    L, U, X = map(int, input().split())
    result = 0
    if X < L:
        result = L-X
    elif X > U:
        result = -1

    print("#{} {}".format(tc, result))
