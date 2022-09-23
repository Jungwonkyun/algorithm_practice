from itertools import combinations

N = int(input())
power = []
member = []
selected = [0]*N

for i in range(N):
    temp = list(map(int,input().split()))
    power.append(temp)

for i in range(N):
    member.append(i)

# 집합 2개로 나누는 모든 경우의 수를 구한다
nCr = list(combinations(member,N//2))
mini = 1e+9

for i in range(len(nCr)):
    A = set(nCr[i])
    B = set(member)-A #set B는 member - A 차집합
    
    power1 = 0
    power2 = 0

    for j in A:
        for k in A:
            power1 += power[j][k]
    
    for j in B:
        for k in B:
            power2 += power[j][k]    

    diff = abs(power1-power2)
    
    if diff < mini:
        mini = diff 

print(mini)

    




    
    

