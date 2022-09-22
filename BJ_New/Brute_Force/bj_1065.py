N = int(input())
cnt = 0

for num in range(1,N+1):

    str_num = str(num)
    
    if num < 100:
        cnt+=1
        continue

    else:
        diff = int(str_num[0]) - int(str_num[1])
        
        for i in range(1,len(str_num)):
            now_diff = int(str_num[i-1]) - int(str_num[i])
            if diff != now_diff:
                break 
            else:
                diff = now_diff
                if i == (len(str_num)-1):
                    cnt+=1

print(cnt)
