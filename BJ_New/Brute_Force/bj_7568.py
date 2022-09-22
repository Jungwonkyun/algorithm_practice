N = int(input())
body = [] 
rank = []

for i in range(N): 
    x,y = map(int, input().split())
    temp = [x,y]
    body.append(temp)


for i in range(N):
    cnt = 1
    for j in range(N):
        if body[i][0] < body[j][0] and body[i][1] < body[j][1]:
            cnt+=1 

    print(cnt,end = " ")


