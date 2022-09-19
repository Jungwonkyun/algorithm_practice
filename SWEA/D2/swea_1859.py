T = int(input())
n = 1

for test_case in range(T):
    
    day = int(input())
    price_ary = list(map(int, input().split()))
    profit = 0
    
    #맨 뒤의 값을 max 값으로 잡는다 
    max_value = price_ary [-1]

    #리스트를 거꾸로 확인해가면서 profit계산
    for i in range(len(price_ary)-1,-1,-1):
        
        #이전 가격이 이후 가격보다 높을 경우 이전에 팔아야하므로 max값 변경
        if price_ary[i] >= max_value:
            max_value = price_ary[i]

        #이전 가격이 이후 가격보다 낮을 경우 max값보다 커질 때까지 사는게 이득 
        elif price_ary[i] < max_value:
            profit += max_value - price_ary[i]

    print("#{} {}".format(n,profit))
    n+=1


