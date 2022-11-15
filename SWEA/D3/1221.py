TC = int(input())

for _ in range(TC):
    case, N = map(str,input().split())
    N = int(N)
    num_list = list(map(str,input().split()))
    num_dict = dict()
    alpha = ["ZRO", "ONE", "TWO", "THR", "FOR",
             "FIV", "SIX", "SVN", "EGT", "NIN"]
    for num in num_list:
        num_dict[num] = num_dict.get(num,0)+1
    print(case)
    for alp in alpha:
        for i in range(num_dict[alp]):
            print(alp,end = " ")
