for t in range(1,11):
    length = int(input())
    alpha = []
    result = 0
    for _ in range(8):
        alpha.append(list(map(str,input())))

    #가로 회문 검색
    for y in range(8):
        for x in range(8-length+1):       
            orig = "".join(alpha[y][x:x+length])
            rev = orig[::-1]
            if orig == rev:
                result+=1 

    
    #세로 회문 검색 
    for x in range(8):
        for y in range(8-length+1):
            print(alpha[y:y+length][x])
            orig = "".join(alpha[y:y+length][x])
            rev = orig[::-1]
            if orig == rev:
                result += 1

    print("#{} {}".format(t,result))

        