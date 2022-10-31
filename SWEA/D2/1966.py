test_case = int(input())

for n in range(test_case):
    num_cnt = int(input())
    num_list = list(map(int,input().split()))
    num_list = sorted(num_list)
    print("#{} ".format(n+1),end = "")
    
    for num in num_list:
        print(num,end = " ")
    print()