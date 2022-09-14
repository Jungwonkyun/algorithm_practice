test_case = int(input())
result = 0

for i in range(test_case):

    int_list = list(map(int, input().split()))
    int_list.sort() 
    
    del int_list[0]
    del int_list[-1]

    for j in range(8):
        result += int_list[j]
    
    result = round(result/8)
    
    print("#{} {}".format(i+1,result))

    result = 0