
test_case = int(input())

for _ in range(test_case):
    case = int(input())
    num_list = list(map(int, input().split()))
    num_dict = dict()
    maximum = -1
    result = 0

    # input 받아서 딕셔너리에 저장
    for num in num_list:
        temp = num_dict.get(num, 0)
        num_dict[num] = temp+1
        maximum = max(maximum, temp+1)

    # value 기준 최반값으로 정렬
    num_sort = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)

    # 최빈값이 여러개일 경우를 대비
    temp_list = []
    for item in num_sort:
        x, y = item
        if y == maximum:
            temp_list.append(x)

    print("#{} {}".format(case, max(temp_list)))
