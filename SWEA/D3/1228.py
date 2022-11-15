for tc in range(1, 11):
    orig = int(input())
    orig_list = list(map(str, input().split()))
    change = int(input())
    change_list = list(map(str, input().split()))

    for i in range(len(change_list)):
        if change_list[i] == "I":
            start = int(change_list[i+1])
            num = int(change_list[i+2])
            orig_list = orig_list[:start] + \
                change_list[i+3:i+num+3]+orig_list[start:]

    print("#{}".format(tc), end=" ")
    for i in range(10):
        print(orig_list[i], end=" ")
    print()
