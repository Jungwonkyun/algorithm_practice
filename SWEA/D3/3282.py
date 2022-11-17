test_case = int(input())

for tc in range(1,test_case+1):
    N,K = map(int,input().split())
    dp = [[0]*(K+1) for _ in range(N+1)]
    stuff = [] 
    for i in range(N):
        v,c = map(int,input().split())
        stuff.append((v,c))

    for i in range(1,N+1):
        v,c = stuff[i-1]    
        for j in range(1,K+1):
            #물건이 들어갈 수 있는 경우
            if j >= v:
                #이 물건을 넣지 않을 때 vs 이 물건을 넣기 전 + 이 물건을 넣었을 떄
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-v]+c)
            
            #물건이 들어갈 수 없을 떄
            else:
                #이전 물건 상태를 그대로 가져간다
                dp[i][j] = dp[i-1][j]

    print("#{} {}".format(tc,dp[-1][-1]))


    
