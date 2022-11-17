test_case = int(input())

for tc in range(1, test_case+1):
    N, K = map(int, input().split())
    student = list(range(1, N+1))
    submit = list(map(int, input().split()))

    for sub in submit:
        if sub in student:
            student.remove(sub)

    print("#{}".format(tc), end=" ")
    for stu in student:
        print(stu, end=" ")
    print()
