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
        elif change_list[i] == "D":
            start = int(change_list[i+1])
            num = int(change_list[i+2])
            orig_list = orig_list[:start] + orig_list[start+num:]
        elif change_list[i] == "A":
            num = int(change_list[i+1])
            orig_list += change_list[i:i+num]

    print("#{}".format(tc), end=" ")
    for i in range(10):
        print(orig_list[i], end=" ")
    print()
