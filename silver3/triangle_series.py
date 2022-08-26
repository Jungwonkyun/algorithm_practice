# Code by 정원균
# BaekJoon #9461

test_case = int(input())

trinagle_DP = [1, 1, 1, 2, 2]

for i in range(5, 100):
    trinagle_DP.append(trinagle_DP[i-1] + trinagle_DP[i-5])


for i in range(test_case):
    case = int(input())
    
    print(trinagle_DP[case-1])
