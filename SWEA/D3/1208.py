for t in range(1, 11):
    times = int(input())
    box = list(map(int, input().split()))
    while times != 0:
        times -= 1
        maximum = max(box)
        minimum = min(box)
        i = box.index(maximum)
        j = box.index(minimum)
        box[i] -= 1
        box[j] += 1

    print("#{} {}".format(t, max(box)-min(box)))
