import itertools

N,S = map(int,input().split())
number = list(map(int,input().split()))

cnt = 0 

for i in range(1,N+1):
    nCr = list(itertools.combinations(number,i))
    
    for j in range(len(nCr)):
        ncr = list(nCr[j])
        temp = 0

        for num in ncr:
            temp += num
        
        if temp == S:
            cnt+=1 

print(cnt)

