test_case = int(input())
check = ["CEFGHIJKLMNSTUVWXYZ", "ADOPQR", "B"]

for tc in range(1, test_case+1):
    l, r = map(str, input().split())
    if len(l) != len(r):
        print("#{} {}".format(tc, "DIFF"))
        continue

    left, right = [], []
    for i in range(len(l)):
        left.append(l[i])
        right.append(r[i])

    flag = "DIFF"
    for i in range(len(left)):
        for j in range(3):
            # 같은 그룹안에 있으면
            if left[i] in check[j] and right[i] in check[j]:
                flag = "SAME"
                break
            flag = "DIFF"
        if flag == "DIFF":
            break

    print("#{} {}".format(tc, flag))
