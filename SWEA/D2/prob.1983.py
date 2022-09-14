
test_case = int(input())
Grade = ["A+","A0", "A-","B+","B0","B-","C+","C0","C-","D0"]

for i in range(test_case):
    
    N,K = map(int,input().split())

    total_score = []
    k_score = 0

    for j in range(N):   
        mid,fin,hom = map(int,input().split())
        
        #최종 점수 계산 
        total_score.append(mid*0.35+fin*0.45+hom*0.20) 

    #k번째 평균점수 기억해두기
    k_score = total_score[K-1]  

    #내림차순 정렬
    total_score.sort(reverse=True)
    
    #10명 이상이면 학점이 같은 사람이 생길 수 있다. 
    same = N//10
    final_index = total_score.index(k_score)//same

    
    print("#{} {}".format(i+1,Grade[final_index]))