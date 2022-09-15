test_case = int(input())

for i in range(test_case):
    N,K = map(int,input().split())
    result = 0
    puzzle = []

    for j in range(N):
        temp = list(map(int,input().split()))
        
        #양 옆 0벽으로 감싸기
        puzzle.append([0]+temp+[0])


    #위, 아래 0벽으로 감싸기 
    puzzle = [[0]*(N+2)] + puzzle + [[0]*(N+2)]

    #가로로 글자 수 계산 
    for k in range(1,N+2):
        cnt = 0
        for l in range(1,N+2):           
            #if 하얀 글자칸
            if puzzle[k][l] == 1:
                cnt += 1       
            #else 검정 글자칸 
            else:
                if cnt == K:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0

    #세로로 글자 수 계산 
    for k in range(1,N+2):
        cnt = 0
        for l in range(1,N+2):           
            #if 하얀 글자칸
            if puzzle[l][k] == 1:
                cnt += 1            
            #else 검정 글자칸 
            else:
                if cnt == K:
                    result += 1
                    cnt = 0
                else:
                    cnt = 0
                            
    print("#{} {}".format(i+1,result))
