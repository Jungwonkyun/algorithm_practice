N = int(input())
info =[[0,0]for i in range(N)] 
DP = [0]*(N+1)


for i in range(N):
    x,y = map(int,input().split())
    info[i][0] = x
    info[i][1] = y


for i in range(N-1,-1,-1):

    if i+info[i][0] <= N:
        DP[i] = max(DP[i+info[i][0]]+info[i][1],DP[i+1])
       
    else:
        DP[i] = DP[i+1]

print(max(DP))
