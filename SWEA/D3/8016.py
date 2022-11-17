test_case = int(input())

for tc in range(1, test_case+1):
    x = int(input())

    # 초깃값 세팅
    N = 1
    K = 1
    dn = 2
    dk = 6

    for i in range(x-1):
        N += dn
        K += dk
        dn += 4
        dk += 4

    print("#{} {} {}".format(tc, N, K))
