test_case = int(input())

for n in range(test_case):
    N, M = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    result = 0

    if len(list1) == len(list2):
        for i in range(len(list1)):
            result += list1[i]*list2[i]

    elif len(list1) < len(list2):
        while len(list1) <= len(list2):
            temp = 0
            for i in range(len(list1)):
                temp += list1[i]*list2[i]
            result = max(result, temp)
            list1.insert(0, 0)

    else:
        while len(list2) <= len(list1):
            temp = 0
            for i in range(len(list2)):
                temp += list1[i]*list2[i]
            result = max(result, temp)
            list2.insert(0, 0)


    print("#{} {}".format(n+1, result))
