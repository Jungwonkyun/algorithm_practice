# Code by 정원균
# BaekJoon #11053

num_series = int(input())
dp = [0 for i in range(num_series)]

temp = input().split()
series = list(map(int, temp))

for i in range(num_series):
    for j in range(i):
        if (dp[j] > dp[i]) and (series[i] > series[j]):
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
