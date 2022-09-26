import sys
sys.setrecursionlimit(1000000)

N = int(input())
area = []

#정상인 
def DFS(y,x):

    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    visited[y][x] = 1
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<len(area[0]) and 0<=ny<len(area):
            if visited[ny][nx] == 0 and area[ny][nx] == temp: 
                DFS(ny,nx)
                

    return None 


for i in range(N):
    temp = list(map(str,input()))
    area.append(temp)

cnt1 = 0
cnt2 = 0
visited = [[0]*N for _ in range(N)]

#정상인 버전
for y in range(N):
    for x in range(N):
        temp = area[y][x]        
        if visited[y][x] == 0:
            DFS(y,x)
            cnt1+=1

visited = [[0]*N for _ in range(N)]

#적록색맹은 R과 G가 같기 떄문에 R을 전부 G로 바꿔준다. 
for y in range(N):
    for x in range(N):
        if area[y][x] == "R":
            area[y][x] = "G"

#적록색맹 버전 
for y in range(N):
    for x in range(N):
        temp = area[y][x]        
        if visited[y][x] == 0:
            DFS(y,x)
            cnt2+=1
       
print("{} {}".format(cnt1,cnt2))