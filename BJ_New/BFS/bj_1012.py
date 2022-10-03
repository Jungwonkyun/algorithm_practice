from collections import deque

test_case = int(input())

def bfs(y,x):

    cabbage_queue = deque() 
    cabbage_queue.append((y,x)) 

    #기본 틀은 DFS와 비슷하다
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    while cabbage_queue:
        y,x = cabbage_queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and cabbage[ny][nx] == 1:         
                #조건에 부합하면 queue에 넣고 BFS돌린다 
                cabbage_queue.append((ny,nx))
                cabbage[ny][nx] = -1
    return None


for i in range(test_case):
    M,N,K = map(int,input().split())
    cabbage = [[0]*M for _ in range(N)] 
    worm = 0

    for j in range(K):
        x,y = map(int,input().split())
        cabbage[y][x] = 1  

    for y in range(N):
        for x in range(M):
            if cabbage[y][x] == 1:
                worm += 1 
                bfs(y,x)

    print(worm)