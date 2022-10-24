test_case = int(input())

for n in range(test_case):
    day = int(input())
    profit = 0
    stock = list(map(int,input().split()))

    check = 0
    for i in range(day-1,-1,-1):

        if stock[i]>check:
            check = stock[i]
        
        else:
            profit += check - stock[i]

    print("#{} {}".format(n+1,profit))

        
 
