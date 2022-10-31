test_case = int(input())

day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for n in range(test_case):
    m1, d1, m2, d2 = map(int, input().split())
    total = 0
    for i in range(m1, m2+1):
        if i == m1:
            total += day[i] - d1+1

        elif i == m2:
            total += d2

        else:
            total += day[i]

    print("#{} {}".format(n+1, total))
