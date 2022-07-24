num_stair = int(input())
stair_list = [0 for i in range(301)]
sum_DP = [0 for i in range(301)]

for i in range(num_stair):
    temp = int(input())
    stair_list[i+1]=temp

sum_DP[1] = stair_list[1]
sum_DP[2] = stair_list[1]+stair_list[2]

if num_stair >= 3:
    for n in range(3,num_stair+1):
        sum_DP[n] = max(sum_DP[n-2]+stair_list[n],sum_DP[n-3]+stair_list[n-1]+stair_list[n])

print(sum_DP[num_stair])


