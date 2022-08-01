# Code by 정원균
# BaekJoon #1912 

num_series = int(input())
max_sum  = []

temp = input().split()
series = list(map(int, temp))

max_sum.append(series[0])

if num_series == 1: 
    pass

else: 
    for i in range(1,num_series):
        if series[i] + max_sum[i-1] > series[i]:
            max_sum.append(series[i] + max_sum[i-1])
        else:
            max_sum.append(series[i])

print(max(max_sum))
        
