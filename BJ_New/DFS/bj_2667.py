import sys
sys.setrecursionlimit(10000) 

N = int(input())
apart = []
results = []

def DFS(y,x):
    global result 
    apart[y][x] = -1

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<len(apart[0]) and 0<=ny<len(apart) and apart[ny][nx] == 1 :
            result += 1 
            DFS(ny,nx)
            
    return result


for i in range(N): 
    temp = list(map(int,input()))
    apart.append(temp) 

cnt = 0 


for y in range(N):
    for x in range(N):
        node = apart[y][x]
        if node == 1:
            result = 1 
            results.append(DFS(y,x))
            cnt+=1 
        
print(cnt)
results.sort() 

for num in results:
    print(num)
