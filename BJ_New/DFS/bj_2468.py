import sys
sys.setrecursionlimit(10**7) 

N = int(input())
city = [] 
max_safety = 0

def DFS(y,x):

    visited[y][x] = -1

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<len(city[0]) and 0<=ny<len(city):
            #내린 비보다 숫자가 높은 도시에 대해서만 DFS를 진행한다 
            if rain < city[ny][nx] and visited[ny][nx] == 0: 
                DFS(ny,nx)
            
    return None

for i in range(N):
    temp = list(map(int,input().split()))

    if max_safety < max(temp):
        max_safety = max(temp)

    city.append(temp)


result = 0

for rain in range(max_safety+1):
    visited = [[0]*N for _ in range(N)] 
    cnt = 0 
    for y in range(N):
        for x in range(N): 
            #내린 비보다 숫자가 높은 도시에 대해서만 DFS를 진행한다 
            if rain < city[y][x] and visited[y][x] == 0: 
                DFS(y,x)
                cnt+=1 
    
    if result < cnt:
        result = cnt 


print(result)

    
    


