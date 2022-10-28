test_case = int(input())
result = 0

for i in range(test_case):
    input_num = int(input())

    #짝수 일 떄 
    if input_num%2 == 0:
        result = -input_num//2
    #홀수 일 때
    else: 
        result = -(input_num//2)+input_num    
    
    print("#{} {}".format(i+1,result))