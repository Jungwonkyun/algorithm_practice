from collections import deque

N,M  = map(int, input().split())
maze = [] 

def BFS(y,x):

    maze_queue = deque() 
    maze_queue.append((y,x)) 

    #기본 틀은 DFS와 비슷하다
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while maze_queue:
        y,x = maze_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and maze[ny][nx] == 1:         
                #조건에 부합하면 queue에 넣고 BFS돌린다 
                maze_queue.append((ny,nx))
                
                #미로의 다음 좌표를 현재좌표에 +1 
                maze[ny][nx] = maze[y][x]+1 

    #다 끝난 후 좌표는 그 좌표로 갈 수 있는 최단거리를 의미한다
    return maze[N-1][M-1]


for i in range(N):
    maze.append(list(map(int,input())))

print(BFS(0,0))


