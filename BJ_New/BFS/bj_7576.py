from collections import deque

M,N = map(int,input().split())
tomato = []
tomato_queue = deque() 

def bfs(y,x):
    
    #기본 틀은 DFS와 비슷하다
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while tomato_queue:
        y,x = tomato_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and tomato[ny][nx] == 0:         
                #조건에 부합하면 queue에 넣고 BFS돌린다 
                tomato_queue.append((ny,nx))
                tomato[ny][nx] = tomato[ny][nx]+1
    return None


for i in range(N):
    tomato.append(list(map(int,input().split())))

for y in range(N):
    for x in range(M): 
        if tomato[y][x] == 1:
            tomato_queue.append((x,y))
