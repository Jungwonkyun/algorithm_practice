import sys
sys.setrecursionlimit(10000) 

def DFS(map_list,y,x):

    map_list[y][x] = -1 

    #상하좌우 대각선
    dx = [0,0,-1,1,1,1,-1,-1]
    dy = [-1,1,0,0,1,-1,1,-1]

    for i in range(8):
        nx = x+dx[i]
        ny = y+dy[i]
        
        #범위 check
        if 0<=nx<len(map_list[0]) and 0<=ny<len(map_list) and map_list[ny][nx] == 1: 
            DFS(map_list,ny,nx)
                
    return None


        
while True:
    M,N = map(int,input().split())
    
    if N == 0 and M == 0:
        break 

    Map = [] 

    for i in range(N):
        temp = list(map(int,input().split()))
        Map.append(temp)

    cnt = 0
    
    for y in range(N):
        for x in range(M):
            if Map[y][x]  == 1:
                DFS(Map,y,x)
                cnt += 1 

    print(cnt)


    