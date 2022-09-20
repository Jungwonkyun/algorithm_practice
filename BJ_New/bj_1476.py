
E,S,M  = map(int,input().split())
i = 0
j = 0
k = 0
finish = False

cnt = 0

while(finish==False):
    
    i+=1
    j+=1
    k+=1
    cnt+=1

    if i == 16:
        i = 1
    if j == 29:
        j = 1
    if k == 20:
        k = 1
    
    if i == E and j == S and k == M:
        finish = True 

print(cnt)