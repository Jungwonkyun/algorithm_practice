test_case = int(input())

for tc in range(1, test_case+1):
    N, M = map(int, input().split())
    set1 = set(map(str, input().split()))
    set2 = set(map(str, input().split()))

    inter = set1.intersection(set2)
    print("#{} {}".format(tc, len(inter)))
