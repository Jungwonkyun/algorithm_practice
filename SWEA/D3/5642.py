test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    dp = [0]*N
    dp[0] = max(num_list[0], 0)
    result = 0
    for i in range(1, N):
        dp[i] = max(dp[i-1]+num_list[i], dp[i])

    result = max(dp)
    # 모두 음수일 경우 dp의 모든 원소가  0이된다
    if dp == [0]*N:
        result = max(num_list)

    print("#{} {}".format(tc, result))
