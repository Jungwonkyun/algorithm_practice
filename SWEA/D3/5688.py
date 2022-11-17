T = int(input())

for tc in range(1, T + 1):

    N = int(input())
    s, e = 1, N
    ans = -1

    while s <= e:
        mid = (s + e) // 2
        if N == mid ** 3:
            ans = mid
            break
        elif N < mid ** 3:
            e = mid - 1
        else:
            s = mid + 1

    print("#{} {}".format(tc, ans))
