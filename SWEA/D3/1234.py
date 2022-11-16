for TC in range(1, 11):
    N, password = map(str, input().split())
    N = int(N)
    flag = True
    while N:
        if flag == False:
            break

        for i in range(N-1):
            if password[i] == password[i+1]:
                password = password[:i]+password[i+2:]
                N = len(password)
                flag = True
                break

            if i == N-2:
                flag = False
                break

    print("#{} {}".format(TC, password))
