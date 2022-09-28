import sys
sys.setrecursionlimit(10**5) 

N,M = map(int,input().split())
ice  = [] 

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def dfs(y,x):

    visited[y][x] = -1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<M and 0<=ny<N:
            if visited[ny][nx] == 0 and result[ny][nx] != 0:
                dfs(ny,nx)
                
    return None

for i in range(N):
    ice.append(list(map(int,input().split())))

#원래 좌표에서 바닷물과 닿인 부분을 뺀 값 
result = [[0]*M for _ in range(N)]

#바다와 인접해있는 변에 대한 리스트
zeros = [[0]*M for _ in range(N)]
cnt = 0
iteration = 1 

while cnt==0: 
    #주변에 0으로 둘러쌓인 분면 구하기 
    for y in range(N):
        for x in range(M):
            zero_cnt = 0
            if ice[y][x]!=0:        
                for i in range(4):
                    nx = x+dx[i]
                    ny = y+dy[i] 
                
                    if 0<=nx<M and 0<=ny<N and ice[ny][nx] == 0:
                        zero_cnt+=1 

                zeros[y][x] = zero_cnt

    #바닷물에 닿은 부분의 얼음이 한번에 녹고 난뒤 결과 (1년후)
    for i in range(len(ice)):
        for j in range(len(ice[0])):
            if  ice[i][j] - zeros[i][j] > 0:
                result[i][j] = ice[i][j] - zeros[i][j]
            else:
                result[i][j] = 0

    visited = [[0]*M for _ in range(N)]
    
    #녹고 난후에 DFS를 돌린다. 
    for y in range(N):
        for x in range(M):
            if visited[y][x] == 0 and result[y][x]!= 0:
                dfs(y,x)     
                cnt+=1
    
    if cnt == 0:
        iteration = 0 
        break
    
    if cnt != 1:
        break
    
    if cnt == 1:
        cnt = 0
        ice = result
        iteration += 1
    
print(iteration)
        
