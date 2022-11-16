test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    compare = [1]*N
    for i in range(N):
        pivot = num_list[i]
        for j in range(i):
            if num_list[j] < pivot:
                compare[i] = max(compare[i], compare[j]+1)

    print("#{} {}".format(tc,max(compare)))
