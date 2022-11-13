for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())

    def power(a, m):
        if m == 1:
            return N
        return power(a, m-1)*a

    result = power(N, M)

    print("#{} {}".format(tc, result))
