test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    first = 0
    second = 0
    third = 0

    if N == 1:
        first = 1
        second = 1
        third = 2

    else:
        first = str(N*(N+1)//2)
        second = str((N**2))
        third = str(N*(N+1))

    print("#{} {} {} {}".format(tc, first, second, third))
