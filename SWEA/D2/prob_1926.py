
number = int(input()) 

for num in range(1,number+1):
    
    string = str(num)
    
    #3,6,9가 들어가는 횟수 계산 
    cnt = string.count("3")+string.count("6")+string.count("9")

    #3,6,9가 아니면
    if cnt == 0:
        print(num, end = " ")
        
    #3,6,9에 포함되면
    else:
        print("-"*cnt,end = " ")

    
    
        
        
        
        