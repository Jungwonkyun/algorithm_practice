test_case = int(input())
for tc in range(1, test_case+1):
    N = int(input())
    card = list(map(str, input().split()))
    result = []

    # 짝수일 때
    if N % 2 == 0:
        left = card[:int(N/2)]
        right = card[int(N/2):]

    else:
        left = card[:int(N/2)+1]
        right = card[int(N/2)+1:]

    for i in range(len(right)):
        result.append(left.pop(0))
        result.append(right.pop(0))

    result += left

    print("#{}".format(tc), end=" ")
    for i in range(N):
        print(result[i], end=" ")
    print()
