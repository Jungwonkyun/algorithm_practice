N = int(input())
candy_list = [[] for i in range(N)]

def check_candy(candy_list):
    
    row_max = 0
    col_max = 0

    #row max check
    for i in range(N):
        temp = 1
        for j in range(N-1):
            #인접한 사탕이 같은 사탕이라면 
            if candy_list[i][j] == candy_list[i][j+1]:
                temp += 1
            #인접한 사탕이 다른 사탕이라면
            else:
                temp = 1
        
            #새로운 max값 업데이트 
            if temp > row_max:
                row_max = temp

    #col max check
    for i in range(N):
        temp = 1
        for j in range(N-1):
            #인접한 사탕이 같은 사탕이라면 
            if candy_list[j][i] == candy_list[j+1][i]:
                temp += 1
            #인접한 사탕이 다른 사탕이라면
            else:
                temp = 1
        
            #새로운 max값 업데이트 
            if temp > col_max:
                col_max = temp

    check_max = max(row_max,col_max)

    return check_max



for i in range(N):
    string = input() 
    for j in range(N):
        candy_list[i].append(string[j])

#상하좌우 인덱스
index = [[-1,0],[1,0],[0,-1],[0,1]]

maximum = check_candy(candy_list)

#달라지는 부분 check
for i in range(N):
    for j in range(N):
        for k in range(4): 
            dx = index[k][0]
            dy = index[k][1]

            #index가 초과 되면 pass 
            if i+dx < 0 or i+dx > N-1 or j+dy < 0 or j+dy > N-1:
                continue 

            if candy_list[i][j]!= candy_list[i+dx][j+dy]:
                
                #인접한 캔디가 다르면 서로 swap
                candy_list[i][j],candy_list[i+dx][j+dy] = candy_list[i+dx][j+dy],candy_list[i][j]
                
                #print("change: Row:",i+1," Col:",j+1,"swap:",easy[k])
                temp_max = check_candy(candy_list)

                if temp_max > maximum:
                    maximum = temp_max 
                
                #바꾼 원소 다시 복구
                candy_list[i][j],candy_list[i+dx][j+dy] = candy_list[i+dx][j+dy],candy_list[i][j]
                

print(maximum)

        
            
      
        