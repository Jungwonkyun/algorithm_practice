for t in range(1, 11):
    test = int(input())
    dst = input()
    src = input()
    result = 0

    for i in range(len(src)-len(dst)+1):
        if src[i] == dst[0]:
            cnt = 0
            while True:
                if src[i+cnt] != dst[cnt]:
                    break
                cnt += 1
                if cnt == len(dst):
                    result += 1
                    break

    print("#{} {}".format(t, result))
