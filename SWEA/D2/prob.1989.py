test_case = int(input())
check = 0

for i in range(test_case):
    input_string = input()
    length = len(input_string)//2

    for j in range(length):
        if input_string[j] != input_string[-1-j]:
            check = 0
            break
        else:
            check = 1

    print("#{} {}".format(i+1,check))     
