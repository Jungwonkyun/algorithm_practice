test_case = int(input())

for n in range(test_case):
    prime = [2, 3, 5, 7, 11]
    ex = [0, 0, 0, 0, 0]
    num = int(input())

    start = 0
    while num != 1:
        # 나누어지면
        if num % prime[start] == 0:
            num = num//prime[start]
            ex[start] += 1

        else:
            start += 1
    print(n)
    print("#{}".format(n+1), end="")

    for k in ex:
        print(k, end=" ")
    print()
