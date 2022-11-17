test_case = int(input())

for tc in range(1,test_case+1):
    N,Q = map(int,input().split())
    original = [0]* N
    for q in range(Q):
        L,R = map(int,input().split())
        original[L-1:R] = [q+1]*(R-L+1)

    print("#{}".format(tc),end = " ")
    for i in original:
        print(i,end = " ")
    print()