test_case = int(input())

for t in range(1, test_case+1):
    bus_list = []
    bus_stop = []
    bus_dict = dict()

    for i in range(1, 5001):
        bus_dict[i] = 0

    N = int(input())
    for _ in range(N):
        bus_list.append(set(map(int, input().split())))
    P = int(input())

    for _ in range(P):
        temp = int(input())
        bus_stop.append(temp)

    for item in bus_list:
        start, end = item
        for stop in range(start, end+1):
            bus_dict[stop] += 1

    print("#{}".format(t), end=" ")
    for i in bus_stop:
        print(bus_dict[i], end=" ")
    print()
