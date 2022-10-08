from collections import deque

N = int(input())
grid = []
tonado = deque()
wind_dir = []

# 이동순서 서->남->동->북
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

windx = [
    # left
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
    # down
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # right
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # up
    [1, -1, 2, -2, 0, 1, -1, 1, -1]
    
]
windy = [
    # left
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    # down
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    # right
    [1, -1, 2, -2, 0, 1, -1, 1, -1],
    # up
    [1, 1, 0, 0, -2, 0, 0, -1, -1]
]

rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]

def wind(y,x,dir):
    value = 0
    nx = x+dx[dir]
    ny = y+dy[dir]

    sand = grid[ny][nx] 
    sum_value = 0 

    for i in range(9):
        px = nx + windx[dir][i]
        py = ny + windy[dir][i]
        
        #비율대로 모래 계산 합산
        wind_sand = (sand*rate[i])//100
        sum_value += wind_sand

        #격자 밖으로 나간 모래의 경우에 value에 더해준다 
        if not(0<=px<N and 0<=py<N):
            value+=wind_sand
            continue
        #격자 안에 있다면 원래 값에다가 더해준다
        grid[py][px] += wind_sand

    #a에 저장될 남은 모래
    gx = nx+dx[dir]
    gy = ny+dy[dir]
    a = sand - sum_value 
    
    #a가 격자 밖으로 나가면 합산
    if not(0 <= gx < N and 0 <= gy < N):
        value += a 
    
    #a가 격자 안에 있다면
    else:
        grid[gy][gx] += a 

    #토네이도가 분 지점의 모래는 0
    grid[ny][nx] = 0 
    
    return value


def solve(y, x):

    value = 0

    for i in range(len(wind_dir)):     
        #토네이도 소멸시
        if x == 0 and y == 0:
            break
        
        #격자 밖으로 나간 값 value에 더해주기
        value += wind(y,x,wind_dir[i])
        #다음 토네이도 위치
        x = x+dx[wind_dir[i]]
        y = y+dy[wind_dir[i]]        

    return value

for i in range(N):
    grid.append(list(map(int, input().split())))


direction = [0,1,2,3] 

index = 0 
#1부터 7까지    
for i in range(1,N):
    #같은 거 두번씩 
    for _ in range(2):
        for _ in range(i):    
            #바람부는 순서 리스트에 저장 
            wind_dir.append(direction[(index+4)%4])
        index+=1

for _ in range(N-1):
    wind_dir.append(0)

#처음엔 left 방향회전
print(solve(N//2, N//2))
