test_case = int(input())

for n in range(test_case):
    ori_num = int(input())
    num = ori_num
    cnt = 0
    num_list = []
    while True:
        print(num)
        cnt += 1
        str_num = str(num)
        for i in range(len(str_num)):
            if str_num[i] not in num_list:
                num_list.append(str_num[i])

        if len(num_list) == 10:
            break

        num = (cnt+1)*ori_num

    print("#{} {}".format(n+1, num))
