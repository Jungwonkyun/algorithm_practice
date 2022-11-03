test_case = int(input())


def increase_check(number):
    check = True
    length = len(str(number))
    for i in range(length-1):
        if number[i] > number[i+1]:
            check = False
            break

    return check


for t in range(1, test_case+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    result = -1

    for i in range(len(num_list)-1):
        for j in range(i+1, len(num_list)):
            new_num = num_list[i]*num_list[j]
            if len(str(new_num)) == 1:
                continue
            if increase_check(str(new_num)):
                result = max(result, new_num)
    print("#{} {}".format(t, result))
