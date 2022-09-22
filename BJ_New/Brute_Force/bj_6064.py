test_case = int(input())

for i in range(test_case):
    M,N,x,y = map(int,input().split())

    result = 0
    temp = x
    test_result = False
    
    while temp <= M*N:

        #최소공배수 찾는 문제랑 비슷하게 둘 다 나눠지는 값을 구한다
        if (temp-y)%N == 0 and (temp-x)%M == 0:
            test_result = True
            result = temp
            break

        temp+=M

    if test_result == False: 
        print(-1)
    
    else: 
        print(result)