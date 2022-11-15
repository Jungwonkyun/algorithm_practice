test_case = int(input())


def solve(idx, cur_sum):
    global result
    if idx >= N:
        return

    # 다음 index 더한 값
    temp = cur_sum+num_list[idx]
    if temp == K:
        result += 1

    # 현재 index를 포함하지 않을 때
    solve(idx+1, cur_sum)
    # 현재 index를 포함할 때
    solve(idx+1, temp)


for t in range(1, test_case+1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))
    result = 0
    solve(0, 0)

    print("#{} {}".format(t, result))
