n = int(input())
cust = list(map(int,input().split()))
man, emp = map(int,input().split())

total_count = 0

#각각의 매니저 수를 먼저 뺴준다 
for i in range(len(cust)):
    cust[i] -= man 
        
    if cust[i] < 0:
        cust[i] = 0 
        
    total_count+=1 

#남은 손님이 없을 때 까지 뺴준다 
for people in cust:
    temp = people//emp 

    if people % emp == 0:
        total_count += temp 
    
    else:
        total_count += temp+1

print(total_count)


    


    
    


