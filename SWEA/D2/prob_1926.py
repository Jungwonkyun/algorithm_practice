
number = int(input()) 

for num in range(1,number+1):
    
    string = str(num)
    cnt = string.count("3")+string.count("6")+string.count("9")

    if cnt == 0:
        print(num, end = " ")
    
    else:
        print("-"*cnt,end = " ")

    
    
        
        
        
        