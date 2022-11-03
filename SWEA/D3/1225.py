from collections import deque
for _ in range(2):
    test = int(input())
    num_list = list(map(int, input().split()))
    num_queue = deque()

    for i in range(8):
        num_queue.append(num_list[i])

    cnt = 1
    while True:
        num = num_queue.popleft()
        num -= cnt
        # num 값이 0이거나 1이어서 다음번에 종료되어야 한다면?
        if num <= 0:
            num = 0
            num_queue.append(num)
            break

        num_queue.append(num)
        cnt += 1

        if cnt == 6:
            cnt = 1

    print("#", test, end=" ")
    while num_queue:
        print(num_queue.popleft(), end=" ")

    print()
