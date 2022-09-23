from itertools import combinations

N,M = map(int,input().split())
chicken_map = [] 
chicken = []
house = []

for i in range(N):
    temp = list(map(int,input().split()))
    chicken_map.append(temp)


for i in range(N):
    for j in range(N):
        #치킨집 좌표 구하기 
        if chicken_map[i][j] == 2:
            temp = [i,j] 
            chicken.append(temp)
        #가정집 좌표 구하기 
        elif chicken_map[i][j] == 1:
            temp = [i,j] 
            house.append(temp)


result = 10000000

for nCr in combinations(chicken,M):
    ncr = list(nCr)
    temp = 0
    
    for h in house:
        chi_len = 999
        for c in ncr:
            chi_len = min(chi_len,abs(h[0]-c[0])+abs(h[1]-c[1]))
        
        temp += chi_len
    
    result = min(result,temp)

print(result)