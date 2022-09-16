test_case = int(input())

for i in range(test_case):
    
    hour1,min1,hour2,min2 = map(int,input().split())

    min_total = min1 + min2 
    hour_total = hour1+hour2

    #60분이 넘으면 1시간으로 넘겨주기    
    if min_total >= 60:
        min_total = min_total - 60 
        hour_total+=1 
    
    # 12가 넘으면 시간 총합에서 12빼주기 
    if hour_total > 12:
        hour_total = hour_total - 12
    
    print("#{} {} {}".format(i+1,hour_total,min_total))