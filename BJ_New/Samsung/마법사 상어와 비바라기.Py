from collections import deque

N,M = map(int,input().split())
MAP = []
move = []
cloud = [] 

dx = [0,-1,-1,0,1,1,1,0,-1]
dy = [0,0,-1,-1,-1,0,1,1,1]

#대각선 방향 물 체크
check_x = [-1,1,-1,1]
check_y = [-1,-1,1,1]

def moving():

    global cloud 

    #움직일 모든 경우의 수에 따라서 
    for i in range(len(move)):
        visited = [[False]*N for _ in range(N)]
        
        new_cloud = []     
        for j in range(len(cloud)):
            y,x = cloud[j]
            d, velo = move[i]

            #행과 열이 모두 연결되어 있으므로 
            ny = (y+velo*dy[d])%N 
            nx = (x+velo*dx[d])%N 
            
            #구름이 생긴곳 물 양 1 증가
            MAP[ny][nx] += 1          
            
            visited[ny][nx] = True
            #이동후 구름 좌표 temp에 넣어준다 
            new_cloud.append((ny,nx))

        for j in range(len(new_cloud)):
            #대각선 물 체크
            y,x = new_cloud[j]
            for k in range(4):
                gx = x+check_x[k]
                gy = y+check_y[k]

                if 0 <= gx < N and 0 <= gy < N and MAP[gy][gx] != 0:
                    MAP[y][x] += 1

        cloud = []
        
        for y in range(N):
            for x in range(N):
                if visited[y][x] == False and MAP[y][x]>=2:
                    cloud.append((y,x))
                    MAP[y][x]-=2 

    return None


def make_cloud():
    
    #initial cloud
    cloud.append((N-1,0))
    cloud.append((N-1,1))
    cloud.append((N-2,0))
    cloud.append((N-2,1)) 

    moving()

    result = 0 
    for item in MAP:
        result += sum(item)

    print(result)

    return None


for i in range(N):
    MAP.append(list(map(int,input().split())))

for i in range(M):
    move.append(list(map(int, input().split())))

make_cloud()
