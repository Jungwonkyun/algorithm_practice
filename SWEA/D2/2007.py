test_case = int(input())

for n in range(test_case):
    string = input()
    result = 1

    for length in range(1, 11):
        basic = string[0:length]
        start = length
        check = string[length:length*2]

        if basic != check:
            continue
        else:
            result = length
            break

    print("#{} {}".format(n+1, result))
