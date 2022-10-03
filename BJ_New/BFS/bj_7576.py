from collections import deque

M,N = map(int,input().split())
tomato = []
tomato_queue = deque() 

def bfs():
    
    #기본 틀은 DFS와 비슷하다
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while tomato_queue:
        print(tomato_queue)
        y,x = tomato_queue.popleft()
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and tomato[ny][nx] == 0:         
                #조건에 부합하면 queue에 넣고 BFS돌린다 
                tomato_queue.append((ny,nx))
                tomato[ny][nx] = tomato[y][x]+1
    
    return None


for i in range(N):
    tomato.append(list(map(int,input().split())))

for y in range(N):
    for x in range(M): 
        #미리 큐에 넣어두고 bfs를 돌리면 토마토가 1개 초과일때도 처리가 가능하다
        if tomato[y][x] == 1:
            tomato_queue.append((y,x))

bfs()
minimum = 0
for item in tomato:  
    if 0 in item:
        minimum = 0
        break
    
    if max(item)>minimum:
        minimum = max(item)

print(minimum-1)


