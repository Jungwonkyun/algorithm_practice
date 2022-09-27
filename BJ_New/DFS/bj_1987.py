#다시풀기 

import sys
sys.setrecursionlimit(10**7) 

R,C = map(int,input().split())
board = [] 

def DFS(y,x):

    global maximum,cnt 
    route.add(board[y][x])

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]

    for i in range(4):
        nx = x+dx[i] 
        ny = y+dy[i] 

        if 0<=nx<C and 0<=ny<R:
            if board[ny][nx] not in route:
                
                cnt += 1 
                #print("Go DFS ny:{} nx:{} value: {}".format(ny,nx,board[ny][nx]))
                DFS(ny,nx)
                visited[ny][nx] = 0

        length = len(route)
        #print(route)
        #print(length)
        
        if length > maximum:
            maximum = length

        
    route.remove(board[y][x])
        
    return None

for i in range(R):
    board.append(list(map(str,input())))

route = []
maximum = 0 
cnt = 1 
visited = [[0]*C for _ in range(R)]
DFS(0,0)

print(maximum)