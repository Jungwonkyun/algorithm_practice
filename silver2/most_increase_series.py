
num_series = int(input())
longest = [] 
dp = [0]*num_series

temp = input().split()
series = list(map(int,temp))


for i in range(num_series):     
    cur_max = series[i]
    cnt = 1     
    for j in range(i+1,num_series):
        if series[j] > cur_max:
            cur_max = series[j]
            cnt+=1 
    dp[i] = cnt     

print(max(dp))

    