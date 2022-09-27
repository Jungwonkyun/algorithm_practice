import sys
sys.setrecursionlimit(10**7) 

M,N,K = map(int,input().split())

#여기는 직사각형이 들어올 좌표 
rectangle = [] 

#전체 모눈 종이 좌표, 직사각형이 겹치는 곳은 1이 된다 
total = [[0]*N for i in range(M)]

def dfs(y,x):

    global area
    visited[y][x] = -1 

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx<N and 0<=ny<M:
            #참고 dfs를 보내는 조건 값과 여기서 다시 돌리는 조건 값은 같아야함 
            if visited[ny][nx] == 0 and total[ny][nx] == 0:
                area += 1
                dfs(ny,nx)

    return None 

for i in range(K):
    rectangle.append(list(map(int,input().split()))) 

#직사각형에 겹치는 부분은 1로 바꿔줘서 탐색하지 않도록 한다 
for item in rectangle:
    for y in range(item[1],item[3]):
        for x in range(item[0],item[2]):
            total[y][x] = 1 


visited = [[0]*N for _ in range(M)]
area_list = [] 

cnt = 0
for y in range(M):
    for x in range(N):
        area = 1
        #아직 탐색 x 이면서 직사각형 안에 없는 좌표만 탐색 
        if visited[y][x] == 0 and total[y][x] == 0: 
            dfs(y,x)
            cnt+=1 
            area_list.append(area)

area_list.sort()         
print(cnt)

for num in area_list:
    print(num,end = " ")



