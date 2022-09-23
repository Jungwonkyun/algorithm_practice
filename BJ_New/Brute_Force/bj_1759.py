import itertools

r,n  = map(int, input().split())
alphabet = sorted(input().split()) 
vowel = ["a","e","i","o","u"]
possible = []

#순서 상관없이 문자만 뽑으면 되므로 조합 사용
nPr = list(itertools.combinations(alphabet,r))

for i in range(len(nPr)):
    npr = list(nPr[i]) 
    for j in range(len(npr)-1):
        
        #문자 -> Ascii바꿔주는 내장함수 ord()
        if ord(npr[j]) - ord(npr[j+1]) <= 0:
            if j+1 == len(npr)-1:
                possible.append(npr)
            
            else: continue
        
        else:
            break 

for i in range(len(possible)):
    cnt_v = 0
    cnt_c = 0

    for j in range(r):
        if possible[i][j] == "a" or possible[i][j] == "e" or possible[i][j] == "i" or possible[i][j] == "o" or possible[i][j] == "u":
            cnt_v +=1 
        else:
            cnt_c +=1 

    #모음 최소 1개 자음 최소 2개 조건 확인하기 
    if cnt_v >=1 and cnt_c >= 2:
        string = ""
        for j in range(r):
            string += possible[i][j]
        print(string)
    
