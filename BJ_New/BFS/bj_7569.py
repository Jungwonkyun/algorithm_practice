from collections import deque

M,N,H  = map(int,input().split())
tomato = []
tomato_queue = deque()

def bfs():
    
    #기본 틀은 DFS와 비슷하다
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    dl = [-1,1]

    while tomato_queue:

        l,y,x = tomato_queue.popleft()
        
        #같은 층에서 확인 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<M and 0<=ny<N and tomato[l][ny][nx] == 0:         
                #조건에 부합하면 queue에 넣고 BFS돌린다 
                tomato_queue.append((l,ny,nx))
                tomato[l][ny][nx] = tomato[l][y][x]+1 

        #위, 아래 확인 
        for i in range(2):
            nl = l+dl[i] 

            if 0<=nl<H and tomato[nl][y][x] == 0:
                tomato_queue.append((nl,y,x))
                tomato[nl][y][x] = tomato[l][y][x]+1 

    return None

for i in range(H):
    level = []
    for j in range(N):
        level.append(list(map(int,input().split())))
    tomato.append(level)

#가로, 세로, 층수 3차원 배열로 만들어서 input으로 넣음 
for l in range(H):
    for y in range(N):
        for x in range(M):
            if tomato[l][y][x] == 1:
                tomato_queue.append((l,y,x))
bfs()

maximum = 0 
false_check = True

for l in range(H):
    for y in range(N):
        if 0 in tomato[l][y]:
            maximum = 0
            false_check = False
            break 
        
        else:
            temp = max(tomato[l][y])
            if maximum < temp:
                maximum = temp
    
    if false_check == False:
        break

print(maximum-1)
