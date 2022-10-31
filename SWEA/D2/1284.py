test_case = int(input())

for n in range(test_case):
    P, Q, R, S, W = map(int, input().split())
    result = 0
    price1 = P*W
    price2 = 0

    if W <= R:
        price2 = Q
    else:
        price2 = Q + (W-R)*S

    result = min(price1, price2)

    print("#{} {}".format(n+1, result))
