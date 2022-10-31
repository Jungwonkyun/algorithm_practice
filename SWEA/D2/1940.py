test_case = int(input())

for t in range(test_case):
    second = int(input())
    total = 0
    velocity = 0
    temp = []

    for s in range(second):
        temp.append(input())

    for info in temp:
        #가속 or 감속
        if len(info) == 3:
            di, acc = map(int, info.split())
            # 가속
            if di == 1:
                velocity += acc
            # 감속
            else:
                velocity -= acc
                if velocity < 0:
                    velocity = 0

        else:
            pass

        total += velocity

    print("#{} {}".format(t+1, total))
