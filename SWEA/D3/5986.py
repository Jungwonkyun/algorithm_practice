test_case = int(input())
prime_set = []
for i in range(2, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_set.append(i)

for tc in range(1, test_case+1):
    N = int(input())
    cnt = 0
    for x in range(len(prime_set)):
        if prime_set[x] < N:
            for y in range(x, len(prime_set)):
                if prime_set[x]+prime_set[y] < N:
                    for z in range(y, len(prime_set)):
                        if prime_set[x]+prime_set[y]+prime_set[z] == N:
                            cnt += 1

    print("#{} {}".format(tc, cnt))
