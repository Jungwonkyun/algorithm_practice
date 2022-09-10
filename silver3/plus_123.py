#Code by 정원균 
#BaekJoon #9095

def plus(num):

    dp = [1,2,4]

    count = 3

    if num < 3:
        return dp[num-1]
    
    else:
        while count<num: 
            dp.append(dp[count-3]+dp[count-2]+dp[count-1])
            count+=1
        return dp[num-1]

def main():

    test_case = int(input())

    for i in range(test_case):
        temp = int(input())
        print(plus(temp))

    return None


main()