N = int(input())
start = [0]
end = [0] 
profit = [0]  
DP = [0]*(N+2)

for i in range(1,N+1):
    t,p = map(int,input().split())
    start.append(i)
    end.append(i+t-1)
    profit.append(p)

for time in range(1,N+1):

    #전날까지의 받을 수 있는 수익과 현재 예상 수익을 비교 
    DP[time] = max(DP[time],DP[time-1]) 

    #다음 작업이 휴가 전에 완료할 수 없을 경우
    if end[time] > N:
        continue

    #다음 작업을 지금부터 시작하면 휴가 전에 시작할 수 있는 경우   
    #작업이 끝나는 날의 예상 값과 현재 시점 + 끝나는 날에 얻을 수 있는 수익중에 큰 값으로 변경 
    DP[end[time]+1] = max(DP[end[time]+1], DP[time]+profit[time])
        

answer = 0
for i in range(0, N + 2):
    answer = max(answer, DP[i])

print(answer)

