import itertools

N = int(input())
num_list = list(map(int,input().split()))

nPn = list(itertools.permutations(num_list,N))

maximum = -1 

for i in nPn:
    npn = list(i)
    temp = 0
    
    for i in range(N-1):
        temp += abs(npn[i]-npn[i+1])
    
    if temp > maximum:
        maximum = temp
    
print(maximum)
