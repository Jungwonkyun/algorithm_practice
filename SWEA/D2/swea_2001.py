test_case = int(input())

for i in range(test_case):
    N,M = map(int,input().split())
    fly_ary = []

    for j in range(N):
        temp = list(map(int,input().split()))
        fly_ary.append(temp)

    maximum = 0

    for k in ranges(N-M+1):
        for l in range(N-M+1):
            temp = 0 

            for t in range(k,k+M):
                for m in range(l,l+M):
                    temp += fly_ary[t][m] 
            
            if temp>maximum:
                maximum = temp  

    print("#{} {}".format(i+1,maximum))